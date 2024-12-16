#!/bin/bash

echo "Bem-vindo à calculadora x2"
echo "Digite o primeiro número: "
read num1

echo "Digite o segundo número: "
read num2

echo "Escolha a operação: +, -, *, /"
read op

case $op in
    +) resultado=$(echo "$num1 + $num2" | bc);;
    -) resultado=$(echo "$num1 - $num2" | bc);;
    \*) resultado=$(echo "$num1 * $num2" | bc);;
    /) resultado=$(echo "scale=2; $num1 / $num2" | bc);;
    *) echo "Operação inválida"; exit 1;;
esac

echo "O resultado é: $resultado"
