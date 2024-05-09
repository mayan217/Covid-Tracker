IDENTIFICATION DIVISION.
PROGRAM-ID. Fibonacci-Series.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 Fibonacci-Limit   PIC 9(5).
01 Fibonacci-Array.
   05 Fibonacci-Number   OCCURS 50 TIMES PIC 9(10).
01 Index               PIC 9(5).
01 Counter             PIC 9(5) VALUE 2.

PROCEDURE DIVISION.
    DISPLAY "Enter the limit for Fibonacci series:" 
    ACCEPT Fibonacci-Limit.
    
    IF Fibonacci-Limit < 2
        DISPLAY "Invalid limit. Please enter a number greater than or equal to 2."
        STOP RUN
    END-IF
    
    MOVE 0 TO Fibonacci-Array(1)
    MOVE 1 TO Fibonacci-Array(2)
    
    PERFORM UNTIL Counter > Fibonacci-Limit
        COMPUTE Fibonacci-Number(Counter) = Fibonacci-Number(Counter - 1) + Fibonacci-Number(Counter - 2)
        ADD 1 TO Counter
    END-PERFORM
    
    DISPLAY "Fibonacci series up to " Fibonacci-Limit " terms:"
    PERFORM VARYING Index FROM 1 BY 1 UNTIL Index > Fibonacci-Limit
        DISPLAY Fibonacci-Array(Index)
    END-PERFORM.
    
    STOP RUN.
