subroutine simple_routine(a,b,c)
   implicit none
   DOUBLE PRECISION, intent(in) :: a,b
   DOUBLE PRECISION, intent(out) :: c

   c = a+b

end subroutine simple_routine
