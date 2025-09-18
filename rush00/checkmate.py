def checkmate(board: str):
    rows = board.strip().split("\n")
    n = len(rows)

    # ตรวจสี่เหลี่ยมจัตุรัส
    if any(len(r) != n for r in rows):
        print("Error")
        return

    valid = {"K","Q","B","R","P","."}
    board = [list(r) for r in rows]

    # ตรวจตัวอักษรถูกต้อง + หา King
    kings = []
    for r in range(n):
        for c in range(n):
            if board[r][c] not in valid:
                print("Error")
                return
            if board[r][c]=="K":
                kings.append((r,c))

    if len(kings)!=1:
        print("Error")
        return

    kr, kc = kings[0]

    # ฟังก์ชันช่วยตรวจว่าตัวใดโจมตี King ไหม
    def attacks(r,c,dirs,slide=False):
        for dr,dc in dirs:
            nr,nc = r,c
            while True:
                nr+=dr; nc+=dc
                if not (0<=nr<n and 0<=nc<n):
                    break
                if (nr,nc)==(kr,kc):
                    return True
                if board[nr][nc]!=".":
                    break
                if not slide:
                    break
        return False

    for r in range(n):
        for c in range(n):
            piece = board[r][c]
            if piece=="." or piece=="K":
                continue
            if piece=="P" and attacks(r,c,[(-1,-1),(-1,1)]):
                print("Success"); return
            if piece=="B" and attacks(r,c,[(-1,-1),(-1,1),(1,-1),(1,1)],slide=True):
                print("Success"); return
            if piece=="R" and attacks(r,c,[(-1,0),(1,0),(0,-1),(0,1)],slide=True):
                print("Success"); return
            if piece=="Q" and attacks(r,c,[(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)],slide=True):
                print("Success"); return

    print("Fail")
