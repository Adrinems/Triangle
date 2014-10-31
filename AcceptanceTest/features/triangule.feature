Feature: Obtener el tipo de tríangulo a partir de las medidas de sus lados
	Como usuario del sistema
	Quiero obtener un programa que diga el tipo de triangulo
	para facilitar la identificación del mismo.

Scenario: Triangulo de lados "201", "0", "201"
	Given: Un triangulo de lados "201", "0", "201"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "NotATriangle"

Scenario: Triangulo de lados "8", "1", "3"
	Given: Un triangulo de lados "8", "1", "3"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "NotATriangle"

Scenario: Triangulo de lados "4", "4", "4"
	Given: Un triangulo de lados "4", "4", "4"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "Equilateral"

Scenario: Triangulo de lados "3", "2", "2"
	Given: Un triangulo de lados "3", "2", "2"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "Isosceles"

Scenario: Triangulo de lados "8", "15", "8"
	Given: Un triangulo de lados "8", "15", "8"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "Isosceles"

Scenario: Triangulo de lados "5", "5", "8"
	Given: Un triangulo de lados "5", "5", "8"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "Isosceles"

Scenario: Triangulo de lados "7", "3", "4"
	Given: Un triangulo de lados "7", "3", "4"
	When: realizo el calculo
	Then: obtengo un triangulo de tipo "Scalene"