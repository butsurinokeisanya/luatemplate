Option Explicit

# FizzBuzz問題
Sub fizzbuzz()
    Dim i As Integer
    For i = 1 To 100
        If i Mod 3 = 0 And i Mod 5 = 0 Then
            Debug.Print i & ":FizzBuzz"
        ElseIf i Mod 3 = 0 Then
            Debug.Print i & ":Fizz"
        ElseIf i Mod 5 = 0 Then
            Debug.Print i & ":Buzz"
        Else
            Debug.Print i
        End If
    Next i
End Sub