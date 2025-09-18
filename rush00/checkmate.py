def checkmate(board: str):
    """
    ฟังก์ชันหลัก ตรวจสอบว่า King ถูกเช็คหรือไม่
    """
    rows = board.strip().split("\n")

    # ตรวจว่าบอร์ดเป็นสี่เหลี่ยมจัตุรัส
    n = len(rows)
    if any(len(row) != n for row in rows):
        print("Error")
        return

    board = [list(row) for row in rows]

    # หา King ทั้งหมด
    kings = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                kings.append((r, c))

    # ต้องมี King แค่ 1 ตัวเท่านั้น
    if len(kings) != 1:
        print("Error")
        return

    kr, kc = kings[0]

    for r in range(n):
        for c in range(n):
            piece = board[r][c]
            if piece == "." or piece == "K":
                continue

            # Pawn (โจมตีขึ้นด้านบน)
            if piece == "P":
                for dr, dc in [(-1,-1), (-1,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) == (kr, kc):
                        print("Success")
                        return

            # Bishop
            elif piece == "B":
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    nr, nc = r, c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if board[nr][nc] != ".":
                            if (nr,nc) == (kr, kc):
                                print("Success")
                                return
                            break

            # Rook
            elif piece == "R":
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r, c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if board[nr][nc] != ".":
                            if (nr,nc) == (kr, kc):
                                print("Success")
                                return
                            break

            # Queen
            elif piece == "Q":
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r, c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if board[nr][nc] != ".":
                            if (nr,nc) == (kr, kc):
                                print("Success")
                                return
                            break

    print("Fail")