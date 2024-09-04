nathan@physlin20:~/phys320$ cat 1.1_first.f
C
Code by Nathan Moore
C
C       this program says hello
C       compile with "f77 program.f"
C       the run ./a.out
C
        PRINT *,"Hello!"
        STOP
        END
nathan@physlin20:~/phys320$ f77 1.1_first.f
nathan@physlin20:~/phys320$ ./a.out
 Hello!
nathan@physlin20:~/phys320$
