import cv2
import mediapipe as mp
import pygame
import os
import time


MUSIC_FOLDER = "music"
CAMERA_INDEX = 0


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def load_songs(folder):
    songs = []

    if not os.path.exists(folder):
        os.makedirs(folder)

    for file in os.listdir(folder):
        if file.lower().endswith((".mp3", ".wav", ".ogg")):
            songs.append(os.path.join(folder, file))

    return songs


def count_fingers(hand_landmarks, handedness_label):
    landmarks = hand_landmarks.landmark

    fingers = 0

    # Dedos: índice, medio, anular, meñique
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip, pip in zip(finger_tips, finger_pips):
        if landmarks[tip].y < landmarks[pip].y:
            fingers += 1

    # Pulgar
    if handedness_label == "Right":
        if landmarks[4].x < landmarks[3].x:
            fingers += 1
    else:
        if landmarks[4].x > landmarks[3].x:
            fingers += 1

    return fingers


def get_gesture(fingers_count):
    if fingers_count == 0:
        return "PUÑO"
    elif fingers_count >= 4:
        return "MANO ABIERTA"
    elif fingers_count == 2:
        return "DOS DEDOS"
    else:
        return "GESTO NEUTRO"


def play_song(songs, index):
    if not songs:
        return

    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    print(f"Reproduciendo: {os.path.basename(songs[index])}")


def main():
    songs = load_songs(MUSIC_FOLDER)

    if not songs:
        print("No encontré canciones.")
        print("Agregá archivos .mp3 dentro de la carpeta music/")
        return

    pygame.mixer.init()
    current_song = 0
    is_playing = False

    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    last_action_time = 0
    action_cooldown = 1.2

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        while True:
            success, frame = cap.read()

            if not success:
                print("No se pudo leer la cámara.")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(rgb_frame)

            gesture = "SIN MANO"

            if results.multi_hand_landmarks and results.multi_handedness:
                for hand_landmarks, handedness in zip(
                    results.multi_hand_landmarks,
                    results.multi_handedness
                ):
                    handedness_label = handedness.classification[0].label

                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS
                    )

                    fingers = count_fingers(hand_landmarks, handedness_label)
                    gesture = get_gesture(fingers)

                    current_time = time.time()

                    if current_time - last_action_time > action_cooldown:

                        if gesture == "MANO ABIERTA":
                            if not is_playing:
                                pygame.mixer.music.unpause()
                                if not pygame.mixer.music.get_busy():
                                    play_song(songs, current_song)
                                is_playing = True
                                last_action_time = current_time

                        elif gesture == "PUÑO":
                            if is_playing:
                                pygame.mixer.music.pause()
                                is_playing = False
                                last_action_time = current_time

                        elif gesture == "DOS DEDOS":
                            current_song = (current_song + 1) % len(songs)
                            play_song(songs, current_song)
                            is_playing = True
                            last_action_time = current_time

            cv2.putText(
                frame,
                f"Gesto: {gesture}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                "Mano abierta: Play | Puno: Pausa | Dos dedos: Siguiente | Q: Salir",
                (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            cv2.imshow("Joa DJ :)", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()
    pygame.mixer.quit()


if __name__ == "__main__":
    main()