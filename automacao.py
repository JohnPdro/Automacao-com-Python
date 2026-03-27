import pyautogui

with open('files/alunos.txt', 'r', encoding='utf-8') as file:
    for line in file:
        aluno = line.split(',')[0]
        email = line.split(',')[1]

        pyautogui.click(1613, 562, duration=0.3)
        pyautogui.write(aluno)
        
        pyautogui.click(1613, 600, duration=0.3)
        pyautogui.write(email)
        
        pyautogui.click(1630, 620, duration=0.3)
        
        pyautogui.screenshot(f'files/{aluno}.png')