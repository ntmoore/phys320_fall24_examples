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
nathan@physlin20:~/phys320$ cat bike_ride.f
        implicit none
        integer i, N
        real dt, a, v0, v, x0, x, t
        real dx, one_over_v_sum, v_sum
        N=10
        dt=5.0
        a=1.0
        v0=10
        x0=20
        dx=175

        print *,"regular time sampling"
        print *,"time (s)       v (m/s)       x (m)"
        v_sum=0.0
        do 1 i=1,N
                t = dt*float(i)
                v = v0 + a*t
                x = x0 + v0*t + 0.5*a*t**2
                print *,t,v,x
                v_sum = v_sum + v
 1      continue

                PRINT *,"V_AVG = ",v_sum/float(N)

        print *,"regular distance sampling"
        print *,"time (s)       v (m/s)       x (m)"
        v_sum=0.0
        one_over_v_sum = 0.0
        do 2 i=1,N
                x = x0 + dx*float(i)
                t = (-v0+sqrt(v0**2-4.0*(a/2.0)*(x0-x)))/(2.0*(a/2.0))
                v = v0 + a*t
                print *,t,v,x
                v_sum = v_sum + v
                one_over_v_sum = one_over_v_sum + 1.0/v
 2     continue

        PRINT *,"V_AVG = ",v_sum/float(N)
        PRINT *,"one_over_V_AVG = ",one_over_v_sum/float(N)
        PRINT *,"V_AVG = ",1.0/(one_over_v_sum/float(N))

        PRINT *,"<v> over time integral gives ",v0+(a/2.0)*(float(N)*dt)
        stop
        end
