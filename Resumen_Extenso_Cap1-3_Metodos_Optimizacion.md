# Resumen extenso — Capítulos 1, 2 y 3
### *Apuntes de Métodos de Optimización* (ICS2121, PUC Chile — F. García Aubert y J. Vera Andreo, v9, agosto 2026)

Este resumen cubre en profundidad los tres primeros capítulos del apunte:

- **Capítulo 1** — Introducción: problemas y algoritmos (pp. 5-8)
- **Capítulo 2** — Métodos del Gradiente, Newton y extensiones (pp. 9-48)
- **Capítulo 3** — Métodos de Primer Orden (pp. 49-82)

Se incluyen todas las definiciones, teoremas, algoritmos y ejemplos aplicados de cada sección, con las demostraciones e interpretaciones más importantes.

---

## Capítulo 1. Introducción: problemas y algoritmos

La idea central del capítulo es desmontar la intuición de que "para optimizar basta derivar e igualar a cero". En la práctica esto casi nunca funciona, porque los problemas reales tienen miles o millones de variables, múltiples mínimos locales, restricciones, y ecuaciones que no se pueden despejar algebraicamente. Esto obliga a construir **algoritmos iterativos** que se conformen con una solución *suficientemente buena*, no con la solución exacta.

### 1.1 El problema general

El problema de optimización se escribe de forma genérica como:

```
P)   min f(x)
     x ∈ S
```

con x ∈ ℝⁿ, f: ℝⁿ → ℝ y S ⊂ ℝⁿ el dominio factible. Cuando las restricciones se hacen explícitas, la forma estándar es:

```
P)   min  f(x)
     s.a. g_i(x) ≤ b_i ,  i = 1, ..., m
```

con f: ℝⁿ → ℝ, g_i: ℝⁿ → ℝ. El apunte hace notar que S no siempre se describe mediante fórmulas algebraicas: también puede incorporar restricciones "de naturaleza" de las variables, como x_i ∈ {0,1} (variables binarias) u otras condiciones más complejas propias de problemas combinatoriales.

### 1.2 Soluciones aproximadas

Se parte suponiendo el caso más simple: S = ℝⁿ (sin restricciones) y f derivable sin problemas. En ese caso el óptimo x* satisface ∇f(x*) = 0. Sin embargo, esta condición es insuficiente en la práctica por tres razones:

1. Pueden existir **múltiples mínimos locales** donde el gradiente también se anula.
2. En problemas reales hay **restricciones**, y la condición de gradiente nulo puede no darse en el óptimo factible.
3. Muchas funciones tienen **miles o millones de variables**, así que "resolver" ∇f(x)=0 exige resolver sistemas gigantes.

Más aún, incluso en una variable, "derivar e igualar a cero" suele llevar a **ecuaciones trascendentes** sin solución algebraica cerrada. El ejemplo clásico del apunte es:

```
f(x) = x² + e^(-x)
f'(x) = 2x - e^(-x) = 0  →  x = (1/2) e^(-x)
```

Esta ecuación no se puede despejar con álgebra elemental. La salida es un **algoritmo de punto fijo**: partiendo de un x₀ arbitrario, se itera

```
x_(k+1) = (1/2) e^(-x_k)
```

hasta que la sucesión converge a un valor cercano al óptimo x*. La moraleja explícita del apunte: *derivar e igualar a cero es generalmente inútil como método de solución; hay que adoptar un enfoque iterativo y aproximado.*

Con esto se formalizan dos nociones de "solución aceptable", que **no son equivalentes pero están relacionadas**:

- **Solución ε-óptima**: x̄ ∈ S tal que |f(x̄) − f(x*)| ≤ ε (el valor objetivo está cerca del óptimo).
- **Solución ε-aproximada**: x̄ tal que ‖x̄ − x*‖ ≤ ε (el propio vector x̄ está cerca de x*).

La relación entre ambas depende de la "curvatura" de f cerca del óptimo: si el gráfico de f es muy plano en torno a x*, una solución ε-aproximada relativamente poco precisa puede igualmente dar una solución ε-óptima muy buena (y viceversa, si f es muy empinada, un pequeño error en x se traduce en un gran error en el valor objetivo).

### 1.3 Algoritmos y oráculos

La idea general es generar una sucesión de puntos x₀, x₁, x₂, … usando en cada paso la iteración anterior más un **oráculo**: una subrutina que entrega información sobre f en un punto dado. Se distinguen tres niveles de oráculo:

| Oráculo | Valores de f | Derivadas (∇f) | Segundas derivadas (∇²f) |
|---|---|---|---|
| Orden cero | ✓ | | |
| Primer orden | ✓ | ✓ | |
| Segundo orden | ✓ | ✓ | ✓ |

Acceder a más información es siempre más costoso computacionalmente, así que un oráculo de orden superior **no es automáticamente más conveniente**: hay que balancear el costo de cada consulta contra cuánto ayuda a reducir el número de iteraciones. Esto introduce el concepto central de **eficiencia/complejidad de un algoritmo**: dado un error aceptable ε > 0, ¿cuántas iteraciones (consultas al oráculo) se requieren para alcanzarlo?

**El problema del oráculo de orden cero.** Si solo se conocen valores de f, evaluar puntos al azar no garantiza acercarse al óptimo: la función puede oscilar y el óptimo puede no estar cerca de los mejores valores ya observados. Esto se puede remediar si se sabe que f satisface una **condición de Lipschitz** con constante L:

```
|f(x) − f(y)| ≤ L|x − y|,  ∀x, y
```

Esta condición acota la pendiente de f: dividiendo por |x−y| y tomando el límite x→y se obtiene |f'(x)| ≤ L para todo x. Gráficamente, la función queda "encajonada" entre dos rectas de pendiente ±L que pasan por cualquier punto conocido. Esto permite **descartar regiones** del dominio: si se conocen los valores de f en puntos suficientemente cercanos entre sí (espaciados en ε/L), se garantiza que en cada subintervalo f no varía más de ε respecto al valor conocido en el extremo.

**Complejidad de la búsqueda por rejilla.** Dividiendo un intervalo [a,b] en p puntos equidistantes con espaciamiento ≤ ε/L, se necesitan p = L/ε evaluaciones para lograr una solución ε-aproximada en una dimensión. La complejidad es, por tanto, del orden **O(L/ε)**: más precisión (ε chico) o una función menos "amable" (L grande) exigen más trabajo.

Al extender esto a n variables, hay que dividir *cada* coordenada, formando una grilla de pⁿ puntos, y evaluar f en todos ellos: la complejidad crece a **O((L/ε)ⁿ)** — la llamada *maldición de la dimensionalidad*. Esto muestra que basarse solo en evaluaciones de la función (oráculo de orden cero) es extremadamente ineficiente en dimensiones altas, y motiva la necesidad de oráculos de mayor orden (gradiente, Hessiano) junto con hipótesis estructurales adicionales sobre f, como la **convexidad** — el puente natural hacia el Capítulo 2.

---

## Capítulo 2. Métodos del Gradiente, Newton y extensiones

Este capítulo aborda el problema irrestricto más simple:

```
P)  min f(x),  x ∈ ℝⁿ
```

con f al menos continuamente diferenciable, y desarrolla los dos métodos clásicos —Gradiente y Newton— junto con sus extensiones Quasi-Newton (BFGS).

### 2.1 La idea del Algoritmo de Descenso

**Definición 2.1.1 (Dirección de descenso).** d ≠ 0 es dirección de descenso de f en x si existe r > 0 tal que f(x + λd) < f(x) para todo λ ∈ (0, r]. Una condición equivalente y más operativa es que la **derivada direccional** sea negativa:

```
dᵀ∇f(x) < 0
```

**Algoritmo genérico del Método de Descenso:**

```
0. x₀ ∈ ℝⁿ, k = 0.
1. Elegir d_k dirección de descenso en x_k.
2. Verificar criterio de parada; STOP si se cumple.
3. λ_k = argmin_{λ≥0} f(x_k + λ d_k)      (linesearch)
4. x_(k+1) = x_k + λ_k d_k,  k ← k+1.  Volver a 1.
```

El criterio de parada habitual es ‖∇f(x_k)‖ < ε, dado que en el óptimo ∇f(x*) = 0 y ∇f(x_k) → 0. El **linesearch** (paso 3) es en sí mismo un problema de optimización, pero unidimensional y por tanto mucho más simple que el problema original. Este esquema básico **solo garantiza convergencia a un mínimo local**, salvo que existan propiedades de convexidad que aseguren que ese local es también global.

Los distintos métodos del capítulo se diferencian únicamente en cómo eligen d_k:
- **Método del Gradiente:** d_k = −∇f(x_k)
- **Método de Newton:** d_k = −[∇²f(x_k)]⁻¹∇f(x_k)
- **Quasi-Newton:** una aproximación distinta de d_k (ver 2.6)

### 2.2 Método del Gradiente

También llamado **Método de Cauchy**. Usa un oráculo de primer orden y toma como dirección la de máximo descenso local, d_k = −∇f(x_k).

```
Algoritmo del Método del Gradiente
0. x₀ ∈ ℝⁿ, k=0, ε>0
1. d_k = −∇f(x_k)
2. Si ‖∇f(x_k)‖ < ε: STOP
3. λ_k tal que ∇f(x_k+λ_k d_k)ᵀ d_k = 0   (linesearch exacto)
4. x_(k+1) = x_k + λ_k d_k, k←k+1. Ir a 1.
```

**Propiedad de ortogonalidad (zig-zag).** Se demuestra que direcciones consecutivas son ortogonales: dₖᵀ dₖ₋₁ = 0, y por tanto ∇f(x_(k+1)) ⊥ ∇f(x_k). La prueba parte de la condición de primer orden del linesearch exacto, ∇f(x+λd)ᵀd = 0, y usando que d_k = −∇f(x_k) se llega en pocos pasos a dₖᵀdₖ₋₁ = 0. Consecuencia práctica: el método **avanza en zigzag**, cambiando de dirección en ángulo recto en cada paso — este comportamiento es la "firma visual" del Método del Gradiente en las curvas de nivel.

**Ejemplo numérico.** Para f(x₁,x₂) = 5x₁² + x₂² + 4x₁x₂ − 14x₁ − 6x₂ + 20 (óptimo en (1,1), f=10), el apunte deriva explícitamente d_k y la fórmula cerrada de λ_k (al ser f cuadrática, el linesearch tiene solución analítica), y muestra tablas e ilustraciones del avance ortogonal partiendo de x₀=(0,10).

El costo del método es bajo: cada iteración solo exige evaluar un gradiente y resolver el linesearch unidimensional (que en la práctica puede aproximarse rápidamente). El apunte incluye un código Python de referencia que implementa el algoritmo para una función cuadrática con un término cuártico adicional, usando `scipy.optimize.fminbound` para el linesearch.

### 2.3 Método de Newton

Usa un oráculo de **segundo orden**. La idea es aproximar f localmente por su polinomio de Taylor de segundo orden y minimizar exactamente esa aproximación.

**Caso escalar.** Aproximando f(y) ≈ f(x) + f'(x)(y−x) + ½f''(x)(y−x)², derivando respecto de y e igualando a cero se obtiene y = x − f'(x)/f''(x), lo que da la iteración:

```
x_(k+1) = x_k − f'(x_k)/f''(x_k)
```

**Caso multivariable.** La aproximación cuadrática es q(y) = f(x) + ∇f(x)ᵀ(y−x) + ½(y−x)ᵀ∇²f(x)(y−x). Minimizándola (∇q(y)=0) se llega a:

```
y = x − [∇²f(x)]⁻¹ ∇f(x)
```

Esto define la dirección de Newton, d_k = −[∇²f(x_k)]⁻¹∇f(x_k). Para que sea una dirección de descenso genuina (∇f(x_k)ᵀd_k < 0) es **necesario que ∇²f(x_k) sea definida positiva** — esto ocurre siempre si f es (globalmente) convexa.

```
Algoritmo del Método de Newton
0. x₀ ∈ ℝⁿ, k=0, ε>0
1. d_k = −[∇²f(x_k)]⁻¹ ∇f(x_k)     (requiere ∇²f(x_k) def. positiva)
2. Si ‖∇f(x_k)‖ < ε: STOP
3. λ_k por linesearch
4. x_(k+1) = x_k + λ_k d_k, k←k+1. Ir a 1.
```

Si f es convexa, Newton converge desde **cualquier** punto inicial al mínimo global. Si solo se sabe que ∇²f(x*) es definida positiva en el óptimo, se tiene únicamente "convexidad estricta local". El código Python de referencia es idéntico al del Gradiente salvo por el cálculo de la dirección, que ahora exige invertir el Hessiano.

### 2.4 Midiendo la eficiencia de un algoritmo

Se introducen dos nociones formales de velocidad de convergencia (con {xᵏ} la sucesión generada, x* el óptimo):

**Definición 2.4.1 (Convergencia lineal).** ‖x_(k+1) − x*‖ ≤ α‖x_k − x*‖, con 0 < α < 1.

**Definición 2.4.2 (Convergencia cuadrática).** ‖x_(k+1) − x*‖ ≤ β‖x_k − x*‖², con β > 0.

**Número de iteraciones requeridas.** Desarrollando ambas recursiones:

- Convergencia lineal: eₖ ≤ αᵏe₀ ⟹ el número de iteraciones para error ≤ ε es del orden **O(log(1/ε))**.
- Convergencia cuadrática: eₖ ≤ β^(2^k − 1) e₀² ⟹ el número de iteraciones necesario es del orden **O(log log(1/ε))**, dramáticamente menor.

Esto formaliza la intuición de que la convergencia cuadrática (Newton) es mucho más rápida en número de iteraciones que la lineal (Gradiente).

#### 2.4.1 Convergencia del Método del Gradiente

Para el problema cuadrático modelo min ½xᵀQx + cᵀx, con Q simétrica y definida positiva, la velocidad de convergencia depende del **número de condicionamiento**:

```
κ(Q) = μ_max / μ_min
```

(μ_max, μ_min: mayor y menor valor propio de Q).

**Teorema 2.4.1.** f(x_(k+1)) − f(x*) ≤ [(κ(Q)−1)/(κ(Q)+1)]² · (f(x_k) − f(x*))

Mientras más grande κ(Q), más "excéntricas" (elípticas alargadas) son las curvas de nivel, más severo el zigzagueo, y más lenta la convergencia. Si κ(Q)=1 (curvas de nivel circulares), Newton... perdón, el **Gradiente** converge en una sola iteración, ya que −∇f(x) apunta directo al centro. El apunte ilustra esto con dos casos numéricos: κ(Q₁)=90,1 (convergencia muy lenta) versus κ(Q₂)=1,85 (mucho más rápida), mostrando las curvas de nivel y las trayectorias correspondientes. El resultado se extiende (informalmente) a funciones convexas generales vía la aproximación cuadrática de Taylor en torno a x*, donde κ pasa a depender de ∇²f(x*).

El número de iteraciones para error ε resulta ser O(log(1/ε)) con constante que depende de α = (κ(Q)+1)/(κ(Q)−1).

#### 2.4.2 Cambios de variable para mejorar el condicionamiento

Se puede mitigar la dependencia en κ(Q) mediante un **cambio de variable lineal** x = Ay. Sustituyendo en f(x)=½xᵀQx+bᵀx se obtiene g(y)=f(Ay), y usando la diagonalización Q = BᵀDB, si se elige A = B⁻¹ se logra que la forma cuadrática quede diagonal (Q̄ = D). Aplicando además y = D^(−1/2)z se llega a una forma perfectamente esférica ½zᵀz. Combinando ambas transformaciones, A = (BD^(1/2))⁻¹ **garantiza que el Gradiente converja en una sola iteración** en el espacio transformado. El costo es que diagonalizar Q exactamente es numéricamente caro; en la práctica se usan aproximaciones parciales de esta idea, lo que se conoce como **precondicionamiento**.

#### 2.4.3 Velocidad de convergencia para el Método de Newton

**Teorema 2.4.2.** Sea f dos veces continuamente diferenciable, x* mínimo local con ∇²f(x*) definida positiva, y supongamos que el Hessiano es localmente Lipschitz cerca de x*: ‖∇²f(x)−∇²f(y)‖ ≤ L‖x−y‖ para x,y en una bola B(x*,r). Entonces existe γ>0 tal que si ‖x₀−x*‖ < γ, la sucesión generada por Newton converge **cuadráticamente**.

Puntos clave de la interpretación:
- Se requiere partir **suficientemente cerca** del óptimo (el radio de convergencia γ depende de L y de ‖[∇²f(x*)]⁻¹‖).
- Contraejemplo instructivo: f(x)=x⁴ es convexa con mínimo en 0, pero f''(0)=0 (Hessiano no definido positivo en el óptimo) ⟹ la convergencia es solo **lineal**, no cuadrática, pese a la convexidad global.
- A diferencia del Gradiente, la sensibilidad de Newton al condicionamiento κ es mucho menor: en la relación cuadrática ‖x_(k+1)−x*‖ ≤ β‖x_k−x*‖², aunque β crezca al aumentar κ, el término cuadrático ‖x_k−x*‖² domina y compensa ese crecimiento — de ahí que Newton sea comparativamente insensible a la excentricidad de las curvas de nivel.

#### 2.4.4 Costo por iteración del Método del Gradiente y Newton

El **tiempo total** de un algoritmo es (número de iteraciones) × (tiempo por iteración), medido en "flops" (operaciones de punto flotante, dominadas por multiplicaciones/divisiones).

- **Gradiente:** x_(k+1) = x_k − λ∇f(x_k) exige una suma y una multiplicación por coordenada ⟹ **O(n)** flops/iteración (asumiendo evaluar ∇f(x) es de costo O(1), modelo de "caja negra").
- **Newton:** requiere invertir el Hessiano (p.ej. vía Eliminación de Gauss-Jordan) ⟹ **O(n³)** flops/iteración.

Combinando con el número de iteraciones:

```
Tiempo total Gradiente ∝ log(1/ε) · n
Tiempo total Newton    ∝ log log(1/ε) · n³
```

Para n muy grande, el factor n³ puede no ser compensado por la ventaja del doble-logaritmo, y **el Método del Gradiente puede terminar siendo más rápido en tiempo real de cómputo**, pese a necesitar muchas más iteraciones. Este balance entre iteraciones y costo por iteración es un tema recurrente en todo el curso (y motiva directamente el Capítulo 3).

### 2.5 Linesearch: Selección del paso

El linesearch resuelve minλ≥0 f(x_k+λd_k) =: min h(λ). Se revisan varios métodos:

**Búsqueda de la Sección Áurea.** Oráculo de orden cero, eficaz si h es *unimodal*. Se eligen 4 puntos en el intervalo con separaciones que satisfacen la razón áurea:

```
φ = (1+√5)/2 ≈ 1,618
```

En cada paso se descarta uno de los extremos según cuál de dos evaluaciones intermedias sea menor, reduciendo el intervalo de búsqueda de forma óptima (garantiza reutilizar uno de los puntos ya evaluados en la siguiente iteración).

**Bisección.** Oráculo de primer orden (usa el signo de h'). Si h'(punto medio) > 0 se busca en la mitad izquierda; si < 0, en la derecha. Reduce el intervalo a la mitad en cada paso.

**Interpolación cuadrática.** Con dos puntos t₁,t₂ y conocidos h(t₁), h(t₂), h'(t₁), se ajusta una parábola g(t)=at²+bt+c resolviendo el sistema 3×3 correspondiente, y se toma como nuevo punto el mínimo analítico t₃ = −b/2a. Se puede iterar (y generalizar a interpolación cúbica, más precisa pero más costosa por iteración).

**Condiciones de Wolfe-Armijo.** La observación clave (Wolfe y Armijo, años 70) es que **no hace falta resolver el linesearch con precisión exacta**: basta que λ cumpla dos condiciones, con h(λ)=f(x_k+λd_k):

```
Armijo (descenso suficiente):  h(λ) ≤ h(0) + c₁λh'(0)
Wolfe   (curvatura):           h'(λ) ≥ c₂h'(0)
```

con 0 < c₁ < c₂ < 1. Armijo garantiza una disminución mínima de f; Wolfe garantiza un avance mínimo (que el paso no sea demasiado corto). Se calcula típicamente mediante **backtracking**: se parte de un λ inicial y se reduce geométricamente (λ_(k+1) = ρλ_k, 0<ρ<1) hasta satisfacer ambas condiciones. Tanto el Método del Gradiente como Newton **mantienen su convergencia** usando pasos que solo satisfacen Wolfe-Armijo, sin necesidad de resolver el linesearch exactamente — esto resulta económico computacionalmente y es lo que se usa en la práctica.

### 2.6 Métodos Quasi-Newton: BFGS

**Motivación.** Newton tiene convergencia cuadrática pero cada iteración cuesta O(n³) por la inversión del Hessiano. Los métodos Quasi-Newton buscan **aproximar** el Hessiano (o su inversa) con una matriz Bᵏ (o Hᵏ = [Bᵏ]⁻¹) simétrica, definida positiva, pero mucho más barata de actualizar y de invertir.

**Condición de secante.** Usando el Teorema del Valor Medio entre iteraciones consecutivas, se exige que la matriz aproximada cumpla:

```
y_k = B^(k+1) s_k,   con  s_k = x_(k+1) − x_k,   y_k = ∇f(x_(k+1)) − ∇f(x_k)
```

Como esta ecuación tiene infinitas soluciones, se elige B^(k+1) como la matriz simétrica, definida positiva, que satisface la condición de secante y que está **lo más cerca posible** de Bᵏ (en cierta norma matricial) — esto exige además la **condición de curvatura** sₖᵀyₖ > 0 para que exista solución definida positiva. Resolviendo este problema (vía Lagrange; ver Nocedal para el detalle) se llega a la fórmula explícita de actualización de la inversa Hᵏ, conocida como **BFGS** (Broyden–Fletcher–Goldfarb–Shanno, años 80):

```
ρ_k = 1 / (y_kᵀ s_k)        (> 0)
H^(k+1) = (I − ρ_k s_k y_kᵀ) H_k (I − ρ_k y_k s_kᵀ) + ρ_k s_k s_kᵀ
```

```
Algoritmo BFGS
0. x₀ ∈ ℝⁿ, H₀ ∈ ℝⁿˣⁿ (p.ej. H₀=I), k=0, ε>0
1. d_k = −H_k ∇f(x_k)
2. Si ‖∇f(x_k)‖ < ε: STOP
3. λ_k por Wolfe-Armijo
4. x_(k+1) = x_k + λ_k d_k
5. Actualizar H_(k+1) por BFGS. k←k+1. Ir a 1.
```

**Costo por iteración: O(n²).** Ordenando cuidadosamente las multiplicaciones (nunca multiplicando matriz×matriz, siempre vector-a-la-vez) el cálculo de Hᵏ⁺¹ se puede hacer en O(n²), muy por debajo del O(n³) de Newton. El apunte detalla explícitamente el orden de operaciones (calcular w=Hᵏyₖ, luego V=wsₖᵀ, U=Hᵏ−ρV, etc., cada paso O(n²)).

**Convergencia superlineal.** Se prueba que ‖x_(k+1)−x*‖/‖x_k−x*‖ → 0, lo que es **más rápido que lineal pero más lento que cuadrático** — de ahí el nombre "super-lineal". En la práctica, BFGS necesita más iteraciones que Newton pero muchas menos que el Gradiente puro, y termina siendo, en general, el **mejor compromiso** entre velocidad de convergencia y costo por iteración — por esto MATLAB y Python (scipy) usan BFGS por defecto para problemas irrestrictos.

**L-BFGS.** Para n muy grande, almacenar la matriz Hᵏ completa es prohibitivo. La variante de **memoria limitada (L-BFGS)** guarda solo un número fijo de pares (sₖ, yₖ) recientes en vez de acumular todos, reconstruyendo una aproximación aceptable de Hᵏ con mucho menor uso de memoria.

**Apéndice: demostración de sₖᵀyₖ > 0 bajo Wolfe-Armijo.** El apunte muestra, partiendo de la condición de Wolfe (∇f(x_(k+1))ᵀd_k ≥ c₂∇f(x_k)ᵀd_k) y usando que d_k es dirección de descenso (∇f(x_k)ᵀd_k < 0) y que (c₂−1) < 0, que necesariamente yₖᵀsₖ > 0 — garantizando que la actualización BFGS mantenga definida positiva la matriz.

### 2.7 Ejemplos de aplicación

El capítulo cierra con siete ejemplos aplicados que ilustran los métodos anteriores en distintos contextos:

**2.7.1 Optimización de Redes Neuronales.** Se modela una red simple: nodos de entrada I, una capa oculta C con activación g(t)=tanh(t), y un nodo de salida s. El entrenamiento se plantea como mínimos cuadrados no lineales sobre los pesos (pesos de entrada→oculta w_ik, de oculta→salida p_ks), minimizando el error entre las salidas predichas v^l y los valores reales v̄^l observados en r puntos de entrenamiento. Como la función no tiene forma analítica simple para su gradiente, se usa **derivación numérica** (diferencias finitas): ∂f/∂yᵢ ≈ [f(y+Δeᵢ,B) − f(y,B)]/Δ. Se entrena con el Método del Gradiente (código Python incluido). **Newton no es adecuado aquí** porque la función (por la no linealidad de tanh) no es convexa y presenta múltiples óptimos locales, haciendo crucial el punto de partida.

**2.7.2 Doblamiento de proteínas.** Se modela una proteína como una cadena de K segmentos rígidos de largo fijo d, articulados en sus extremos. La energía del sistema es Σ aᵢⱼ/distᵢⱼ entre los puntos centrales de los segmentos, y se busca la configuración de mínima energía. Las restricciones de largo fijo (xₖ−xₖ₋₁)² + (yₖ−yₖ₋₁)² = d² se **eliminan por sustitución recursiva**, dejando un problema irrestricto pero muy no lineal. Se discuten ventajas/desventajas de cada método: el **Gradiente** es barato pero lento y la fórmula analítica del gradiente ya es difícil de obtener a mano; **Newton** tiene gran convergencia pero requiere el Hessiano (probablemente numérico), aunque con n del orden de cientos a un par de miles (aminoácidos típicos en proteínas), el costo O(n³) sigue siendo manejable; **BFGS** aparece como el mejor compromiso al requerir solo gradientes.

**2.7.3 Centro Analítico de un Poliedro.** Para P = {x : Ax ≤ b} acotado con interior no vacío, se define la función barrera Φ(x) = −Σ log(bᵢ−aᵢᵀx), cuyo dominio es exactamente el interior de P (Φ→∞ al acercarse a la frontera). Minimizar Φ en el interior de P es, en la práctica, un **problema irrestricto**, porque ningún algoritmo que parta dentro de P puede salir de él sin que Φ diverja. Se calculan explícitamente ∇Φ(x)=AᵀD(x)⁻¹e y ∇²Φ(x)=AᵀD(x)⁻²A (con D(x)=diag(bᵢ−aᵢᵀx)), y se prueba que Φ es estrictamente convexa si A tiene rango completo y m≥n. El método natural es **Newton**, y las condiciones de Wolfe-Armijo automáticamente impiden que el paso salga del poliedro (porque Φ crecería sin límite). Este ejemplo **anticipa los Algoritmos de Punto Interior** para Programación Lineal, tratados en un capítulo posterior.

**2.7.4 Localización espacial.** Se busca ubicar K puntos xₖ ∈ ℝ² de modo de minimizar el costo total ponderado por distancia a m puntos fijos uᵢ: f(x) = ΣₖΣᵢ cᵢₖ‖uᵢ−xₖ‖². La función es convexa cuadrática con **Hessiano diagonal por bloques** (cada bloque de 2×2 depende solo del propio punto k), por lo que el problema se puede **desacoplar en K subproblemas independientes** de 2 variables cada uno, resolubles en paralelo. Esto no solo acelera el cómputo por subproblema, sino que también **mejora el condicionamiento** de cada uno (ya no se ve afectado por valores propios irrelevantes de otras variables), acelerando la convergencia global.

**2.7.5 Estimaciones estadísticas (regresión logística).** Se modela la probabilidad de contagio de una enfermedad como pᵢ = e^(αᵀuᵢ)/(1+e^(αᵀuᵢ)), y se maximiza la log-verosimilitud l(α) = Σ(contagiados) αᵀuᵢ − Σ(todos) log(1+e^(αᵀuᵢ)). Se derivan explícitamente el gradiente y el Hessiano, y se hace un **análisis de esfuerzo computacional en flops**: precomputando e^(αᵀuᵢ) al inicio de cada iteración (O(nm)), el Gradiente cuesta O(nm)/iteración, Newton cuesta O(n³+n²m)/iteración (por formar e invertir el Hessiano n×n), y BFGS cuesta O(nm)/iteración. Combinando con el orden de iteraciones de cada método (Gradiente: O(log 1/ε); Newton: O(log log 1/ε); BFGS: intermedio), se obtiene el costo computacional total de cada enfoque.

**2.7.6 Función Banana (Rosenbrock).** f(x) = Σᵢ b(xᵢ₊₁−xᵢ²)² + (a−xᵢ)², con a=1, b=100. Se muestra que, gracias a su estructura, el gradiente y el Hessiano se calculan en **O(n)** (no O(n²) como sería genérico), porque el Hessiano resulta **tridiagonal** (solo diagonal y sus vecinos inmediatos son no nulos). Se prueba además que ∇f **no es globalmente Lipschitz** (creciendo como t³ a lo largo de una dirección especial), pero **sí lo es en cualquier región acotada** R={‖x‖≤100}, estimando la constante L vía cotas de norma matricial (Frobenius, norma-∞).

**2.7.7 "Newtoncito" y Descenso por Coordenadas.**
- *Algoritmo Newtoncito:* cuando f no es convexa y ∇²f(xₖ) no resulta definida positiva, se ajustan los elementos diagonales de la matriz para forzar que sea **diagonalmente dominante** (lo que garantiza matriz definida positiva, por un teorema citado), asegurando así una dirección de descenso válida incluso para funciones no convexas. Cerca de un mínimo local genuino, la corrección se vuelve innecesaria y el algoritmo se comporta como Newton puro.
- *Descenso por Coordenadas:* para n muy grande donde calcular el gradiente completo es inviable, se elige aleatoriamente una coordenada j₀ y se desciende solo a lo largo de ese eje. Es más barato por iteración pero típicamente requiere muchas más iteraciones que el Gradiente completo. Una variante "combinada" sondea p coordenadas aleatorias para construir una dirección más informada antes de dar el paso, mejorando el rendimiento práctico a bajo costo adicional.

---

## Capítulo 3. Métodos de Primer Orden

El capítulo se motiva con problemas estadísticos de gran escala: sistemas Ax=b con A ∈ ℝ^(m×n), donde en Big Data suele darse **m ≪ n** (subdeterminado, infinitas soluciones). Se busca la solución más "rala" (sparse) posible, lo que lleva a la **regularización L1**:

```
min_x  τ‖x‖₁ + ‖Ax−b‖²
```

Esta función es convexa y continua, pero **no diferenciable** (por ‖x‖₁). Además, con n del orden de cientos de miles o millones de variables, ni el Método de Newton (O(n³)/iteración) ni siquiera el Gradiente clásico con linesearch iterativo son viables. El capítulo desarrolla, entonces, métodos de primer orden **muy baratos por iteración**, extendiéndolos primero a problemas diferenciables de gran escala, y luego a problemas no diferenciables (vía subgradientes) y con restricciones.

### 3.1 Problemas diferenciables

#### 3.1.1 Gradiente sin Linesearch

Se agrega la hipótesis de que f es convexa, continua, diferenciable, **y que ∇f es L-Lipschitz**: ‖∇f(x)−∇f(y)‖ ≤ L‖x−y‖. Usando convexidad se obtiene una **cota inferior lineal**:

```
l_x(y) = f(x) + ∇f(x)ᵀ(y−x) ≤ f(y)
```

y usando la Lipschitzianidad del gradiente se obtiene una **cota superior cuadrática** (sin necesidad de Hessiano):

```
f(y) ≤ f(x) + ∇f(x)ᵀ(y−x) + (L/2)‖y−x‖² =: q_x(y)
```

Minimizando la cota superior q_x(y) respecto de y (derivando e igualando a cero) se obtiene directamente:

```
y = x − (1/L) ∇f(x)
```

— exactamente la forma del Método del Gradiente, pero con **paso fijo λ=1/L, sin resolver ningún linesearch**. Se demuestra que este paso automáticamente satisface las condiciones de Wolfe-Armijo. El único requisito práctico es estimar L (p.ej., el mayor valor propio de ∇²f, o para mínimos cuadrados f(x)=½‖Ax−b‖², L=‖AᵀA‖₂, calculable directamente).

```
Método Simple de Primer Orden (Gradiente sin Linesearch)
x₀ ∈ ℝⁿ, k=0, ε>0
mientras ‖d_k‖ > ε:
    x_(k+1) = x_k + (1/L) d_k
    d_(k+1) = −∇f(x_(k+1))
    k = k+1
```

Este esquema (desarrollado por Nemirovsky en los 70' y completado por Nesterov en los 80') tiene direcciones consecutivas casi colineales (no zig-zaguea ortogonalmente como el Gradiente clásico): el ejemplo de mínimos cuadrados muestra que el producto punto entre direcciones sucesivas suele estar entre 0,9 y 1,0. Esto significa que **avanza casi en línea recta pero con pasos pequeños**, requiriendo muchas más iteraciones — el precio a pagar por no tener que resolver el linesearch.

#### 3.1.2 Convergencia del Método Simple

Se demuestra que, tras k iteraciones:

```
f(x_k) − f(x*) ≤ L‖x₀−x*‖² / (2k)
```

Esto implica que el número de iteraciones necesario para error ε es del orden **O(1/ε)** — **mucho peor** que el O(log(1/ε)) del Gradiente clásico. Sin embargo, como cada iteración es tan barata, el tiempo total puede seguir siendo menor para problemas de gran tamaño, y en muchas aplicaciones (p.ej. entrenar redes neuronales) no se necesita un ε extremadamente pequeño (10⁻² suele bastar). Esto motiva la búsqueda de una versión **acelerada**.

#### 3.1.3 Propiedad fuerte de convexidad

**Definición 3.1.1 (Convexidad fuerte).** f (convexa, con ∇f L-Lipschitz) es fuertemente convexa si existe μ>0 tal que:

```
f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) + (μ/2)‖y−x‖²,  ∀x,y
```

Combinando esta cota inferior con la cota superior L-Lipschitz, f queda "emparedada" entre dos parábolas (una de curvatura μ, otra de curvatura L).

**Teorema 3.1.1.** Bajo convexidad fuerte de parámetro μ y ∇f L-Lipschitz:

```
‖x_(k+1) − x*‖ ≤ [(κ_f − 1)/(κ_f + 1)]^k ‖x_k − x*‖,   κ_f = L/μ
```

Esto es **convergencia lineal**, formalmente análoga a la del Gradiente clásico sobre problemas cuadráticos (con κ_f jugando el rol de κ(Q)) — es decir, O(log(1/ε)) iteraciones. Un resultado de **Nemirovski y Yudin** demuestra —vía un argumento de "oráculo adversario/resistivo"— que **ningún método basado únicamente en direcciones de gradiente puede ser más rápido que esto**: es una cota inferior fundamental para este tipo de algoritmos.

#### 3.1.4 Método acelerado de Nesterov

Nesterov (años 80) diseñó un esquema que usa **dos sucesiones entrelazadas** de puntos, xₖ y zₖ, con un parámetro θₖ decreciente:

```
z_(k+1) = z_k − (1/(θ_k L)) ∇f(θ_k z_k + (1−θ_k) x_k)
x_(k+1) = (1−θ_k) x_k + θ_k z_(k+1)
```

La interpretación: el paso de gradiente se evalúa en un punto **intermedio** entre xₖ y zₖ; al ir decreciendo θₖ, zₖ va "arrastrando" a xₖ con desplazamientos cada vez mayores.

**Teorema 3.1.2.** Con θ_k = 2/(k+2), tras k iteraciones:

```
min_(0≤i≤k) f(x_i) − f(x*) ≤ 2L‖x₀−x*‖² / (k+1)²
```

Esto implica **O(1/√ε)** iteraciones — una mejora sustancial sobre el O(1/ε) del método simple, manteniendo el mismo costo por iteración (una sola evaluación de gradiente). Nótese que la cota es sobre el **mejor valor encontrado hasta la iteración k**, no sobre f(xₖ) directamente, ya que el método **no decrece monótonamente** (puede tener oscilaciones locales, aunque la tendencia global sí sea decreciente). Bajo convexidad fuerte adicional, el método acelerado también alcanza convergencia **lineal**, con constantes aún más favorables que el Gradiente clásico.

### 3.2 Problemas no diferenciables

#### 3.2.1 LASSO (Least Absolute Shrinkage and Selection Operator)

Motivación concreta: en genética estadística, se busca explicar la severidad de una enfermedad (yᵢ) en función de la expresión de n genes (aᵢⱼ) medida en m pacientes, con **n ≫ m**. El sistema y=Ax+e está sobredeterminado en variables (subdeterminado en ecuaciones), y mínimos cuadrados puro no sirve porque da soluciones triviales (múltiples óptimos con valor 0).

La solución conceptual es buscar el vector x con **el menor número de componentes no nulas**:

```
min  card{j : x_j ≠ 0} = ‖x‖₀
s.a. Ax = y
```

Este problema es **combinatorial** (equivalente a programación entera con variables binarias z_j y una constante "Big-M"), e intratable para n grande. La relajación convexa estándar reemplaza ‖x‖₀ por **‖x‖₁ = Σ|xⱼ|** (la mejor aproximación convexa de la "dispersión", mejor que ‖x‖₂ porque la geometría de la bola L1 favorece soluciones en vértices/esquinas con muchas coordenadas exactamente cero). Esto convierte el problema en uno de **Programación Lineal**:

```
min ‖x‖₁   s.a.  Ax = y
```

Y su versión regularizada (irrestricta), la propiamente llamada **LASSO**:

```
min_x  τ‖x‖₁ + ‖Ax−b‖²
```

donde τ>0 balancea dispersión (τ grande → más ceros, peor ajuste) contra bondad de ajuste (τ chico → mejor ajuste, más variables activas).

#### 3.2.2 El Método del Subgradiente

Como ‖x‖₁ no es diferenciable en x=0, se necesita generalizar la noción de derivada.

**Definición 3.2.1 (Subgradiente).** Para f convexa, h ∈ ℝⁿ es subgradiente de f en x si:

```
f(y) ≥ f(x) + hᵀ(y−x),  ∀y
```

**Definición 3.2.2 (Subdiferencial).** ∂f(x) es el conjunto de todos los subgradientes de f en x. Coincide con {∇f(x)} en puntos diferenciables, pero es un **conjunto** (intervalo, en 1D) en puntos "esquina". Condición de optimalidad: x* es mínimo global si y solo si 0 ∈ ∂f(x*).

*Ejemplos:* el subgradiente de |x| es sign(x) para x≠0, y cualquier valor en [−1,1] para x=0. Análogamente para f(x)=max{0, x²−1}.

**Algoritmo del Subgradiente:**

```
x₀ ∈ ℝⁿ, k=0, −d_k ∈ ∂f(x_k), ε>0
mientras no se cumpla criterio de parada:
    elegir paso λ_k
    x_(k+1) = x_k + λ_k d_k
    −d_(k+1) ∈ ∂f(x_(k+1))
    k = k+1
```

*Aplicado a LASSO:* el subgradiente es τ·sgn(x) + 2Aᵀ(Ax−b). En la práctica muchas entradas de x no convergen exactamente a cero sino a valores muy pequeños, que se **redondean a cero**; se calibra τ para lograr un nivel de dispersión (‖x‖₀) deseado sin que el error de ajuste sea excesivo.

**Relación Lipschitz-subgradiente.** Si f es L-Lipschitz, cualquier subgradiente g satisface ‖g‖ ≤ L (demostrado vía la propiedad de "plano soporte" de los subgradientes). Esta relación permite **estimar la constante de Lipschitz** de una función a partir de una fórmula explícita para sus subgradientes, típicamente solo válida en una región acotada de interés.

**Convergencia del Método del Subgradiente.** Suponiendo f L-Lipschitz en una vecindad de radio R en torno a x*, y usando un paso decreciente λ_k = R/(L√(k+1)):

```
min_(0≤i≤k) f(x_i) − f(x*) ≤ RL / √(k+1)
```

lo que implica **O(1/ε²)** iteraciones — considerablemente **peor** que el O(1/ε) del caso diferenciable, ya que los subgradientes contienen mucha menos información estructural que un gradiente verdadero. Esto motiva buscar una variante acelerada.

#### 3.2.3 FISTA (Fast Iterative Shrinkage-Thresholding Algorithm)

Desarrollado por Beck y Teboulle, aplica una idea de aceleración similar a Nesterov a problemas **compuestos** de la forma min g(x)+h(x), con g convexa (posiblemente no diferenciable) y h convexa, diferenciable, con ∇h L-Lipschitz.

```
FISTA
x₀, z₀ ∈ ℝⁿ, k=0, θ₀=1
mientras no se cumpla criterio de parada:
    y_k = z_k − (1/L)∇h(z_k)
    x_(k+1) = argmin_x { g(x) + (L/2)‖x−y_k‖² }
    θ_(k+1) = ½(1 + √(1+4θ_k²))
    z_(k+1) = x_(k+1) + ((θ_k−1)/θ_(k+1))(x_(k+1) − x_k)
    k = k+1
```

*Aplicado a LASSO* (g(x)=τ‖x‖₁, h(x)=‖Ax−b‖²), el subproblema de minimización se **descompone coordenada a coordenada** y tiene solución cerrada de tipo **soft-thresholding**:

```
x_j = sign((y_k)_j) · max{ |(y_k)_j| − τ/L,  0 }
```

La complejidad de FISTA es la misma que la del método acelerado de Nesterov: **O(1/√ε)** iteraciones — una mejora dramática sobre el O(1/ε²) del subgradiente simple, manteniendo un costo por iteración muy bajo. Es ampliamente usado en reconstrucción de imágenes y Compressed Sensing.

#### 3.2.4 Resumen de complejidades

| Problema | Método simple | Método acelerado |
|---|---|---|
| f diferenciable, ∇f L-Lipschitz | O(1/ε) | O(1/√ε) |
| f no diferenciable, f L-Lipschitz | O(1/ε²) | O(1/√ε) (FISTA) |
| f fuertemente convexa, ∇f L-Lipschitz | O(log 1/ε) | O(log 1/ε) |

Los resultados de Nesterov y Nemirovsky muestran que, sin convexidad fuerte, **O(1/√ε) es la mejor tasa alcanzable** por cualquier método basado en un oráculo de primer orden — una cota inferior teórica fundamental.

### 3.3 Métodos de Primer Orden con Restricciones

Se extiende todo lo anterior a problemas min f(x) s.a. x ∈ D, con D convexo.

**El Método Proyectado.** Se define la proyección Π_D(x) = argmin_{y∈D} ‖x−y‖₂, y se modifica la etapa de avance:

```
x_(k+1) = Π_D(x_k + λ_k d_k)
```

Esta idea se aplica igual de bien al Gradiente, al Subgradiente, al método acelerado y a FISTA, **manteniendo las mismas tasas de convergencia** del caso irrestricto — con la condición práctica crucial de que D sea "simple", es decir, que proyectar sobre D sea computacionalmente barato (p.ej., una bola L1 o una caja, donde la proyección es prácticamente cerrada o requiere solo revisar unos pocos vértices).

**Algoritmo de Frank-Wolfe.** Muy usado en Equilibrios de Redes de Transporte y Economía. Aborda problemas del tipo min f(x) s.a. Ax ≤ b, con f convexa diferenciable y ∇f L-Lipschitz. En cada iteración se **linealiza** f en torno a x_k:

```
f(y) ≈ f(x_k) + ∇f(x_k)ᵀ(y − x_k)
```

y se minimiza esa aproximación lineal sobre el mismo poliedro factible (un problema de **Programación Lineal**, resoluble por ejemplo con Simplex):

```
ȳ = argmin_y { ∇f(x_k)ᵀ y : Ay ≤ b }
x_(k+1) = x_k + α_k (ȳ − x_k)
```

con paso α_k = 2/(k+2) (predeterminado, más barato que hacer linesearch).

```
Algoritmo de Frank-Wolfe (paso simple)
x₀ factible, k=0
mientras no se cumpla criterio de parada:
    ȳ = argmin_y { ∇f(x_k)ᵀy : Ay ≤ b }
    x_(k+1) = x_k + (2/(k+2))(ȳ − x_k)
    k = k+1
```

*Aplicación elegante a LASSO restringido* (min‖Ax−b‖² s.a. ‖x‖₁≤ρ): dado que el conjunto factible es un poliedro L1, la solución del subproblema lineal siempre cae en un **vértice** con una sola coordenada distinta de cero (igual a ±ρ) — por lo que el subproblema **no requiere Simplex**, basta recorrer el vector y elegir la mejor entrada. El algoritmo construye la solución **agregando una coordenada no nula a la vez**, calzando perfectamente con el objetivo de dispersión buscado.

**Convergencia:** f(x_k) − f(x*) ≤ 2L·diam(D)²/(k+2), es decir, **O(1/ε)** iteraciones — se puede mejorar con variantes ("away steps") o alcanzar tasa lineal bajo convexidad fuerte.

### 3.4 Ejemplos de aplicación

**3.4.1 Función no diferenciable restringida.** min Σmax{0, xⱼ−αⱼ} + Σxⱼlog(xⱼ) s.a. 1≤xⱼ≤2, combinando un término tipo "bisagra" (no diferenciable) con un término de entropía (diferenciable). Se deriva el subdiferencial por partes y se aplica el Método de Subgradiente Proyectado, con proyección trivial (recorte coordenada a coordenada al intervalo [1,2]) y estimaciones explícitas de R (diámetro de la caja, del orden de √n) y L (cota del subgradiente).

**3.4.2 Subgradiente de la función "Max".** Para f(x) = maxᵢ{aᵢᵀx+bᵢ}, se prueba convexidad (usando que el máximo de una suma está acotado por la suma de máximos), y se muestra que el subdiferencial en un punto x es la **envoltura convexa** de los vectores aᵢ correspondientes a los índices i que alcanzan el máximo en ese punto.

**3.4.3 Subgradiente de función "max" combinada con otras.** Para f(x) = ‖x‖² + Σmax{0, αⱼxⱼ+bⱼ}, el subdiferencial se obtiene sumando el gradiente de la parte diferenciable (2x) con el subdiferencial, coordenada a coordenada, de cada término tipo bisagra.

**3.4.4–3.4.5 Subgradiente y esfuerzo computacional.** Para funciones compuestas más elaboradas (p.ej. xᵀQx + ‖Ax‖² + Σmax{αⱼ,xⱼ⁴}), se descompone el subgradiente por términos aditivos, se acota cada pieza usando desigualdad triangular y normas matriciales (‖Q‖₂, ‖AᵀA‖₂ acotadas vía normas de Frobenius o infinito), y se analiza el costo en flops de cada término (O(n²) para productos matriz-vector, O(n) para términos elemento a elemento).

**3.4.6 Método de Primer Orden proyectado (restricciones de igualdad).** Para min ½xᵀQx+cᵀx s.a. Ax=b, la proyección sobre {Ax=b} tiene solución cerrada vía Lagrangiano:

```
Π(u) = (I − Aᵀ(AAᵀ)⁻¹A) u + Aᵀ(AAᵀ)⁻¹b
```

El análisis de costo muestra que (AAᵀ)⁻¹ se calcula **una sola vez** al inicio (O(n³) amortizado), pero cada iteración sigue costando O(n²) — el mismo orden asintótico que el método sin restricciones, aunque con una constante notablemente mayor (aprox. el doble de trabajo), ilustrando cómo la notación O(·) puede esconder diferencias prácticas relevantes.

**3.4.7 Método no diferenciable proyectado.** Variante del ejemplo estadístico de ajuste lineal Ax=b con restricciones de igualdad adicionales, combinando subgradiente + proyección sobre el mismo tipo de conjunto afín.

**3.4.8 Basis Pursuit.** Se busca representar una función/señal desconocida h como combinación dispersa h=Σxⱼgⱼ de un número enorme de funciones "base" gⱼ conocidas, a partir de m observaciones (h(uᵢ)=yᵢ, con n≫m). Se reconoce como **estructuralmente idéntico a LASSO** (definiendo Aᵢⱼ:=gⱼ(uᵢ)): min τ‖x‖₁ + Σᵢ(Σⱼgⱼ(uᵢ)xⱼ − yᵢ)². Se resuelve con el Método del Subgradiente, derivando explícitamente la parte diferenciable (2Aᵀ(Ax−y)) y la parte tipo signo proveniente de τ‖x‖₁.

---

## Síntesis comparativa de los tres capítulos

- **Capítulo 1** sienta las bases conceptuales: por qué el enfoque analítico ("derivar e igualar a cero") fracasa en la práctica, introduce las nociones de solución ε-óptima/ε-aproximada, y formaliza la complejidad de un algoritmo vía oráculos de orden 0/1/2 y la condición de Lipschitz — mostrando además la maldición de la dimensionalidad de la búsqueda por rejilla.

- **Capítulo 2** desarrolla la optimización clásica irrestricta y diferenciable: el **Gradiente** (barato por iteración, O(n), pero convergencia lineal fuertemente condicionada por κ(Q)); **Newton** (caro por iteración, O(n³), pero convergencia cuadrática, requiriendo convexidad/Hessiano definido positivo y buen punto de partida); y **BFGS/Quasi-Newton** (O(n²) por iteración, convergencia superlineal) como el mejor compromiso práctico. El hilo conductor es siempre el balance **iteraciones × costo por iteración**.

- **Capítulo 3** da el salto al régimen "moderno" de gran escala (Big Data, Machine Learning, Compressed Sensing), donde n puede ser de cientos de miles o millones, volviendo inviables incluso los métodos O(n²)/O(n³). Se privilegian métodos de primer orden con **paso fijo, muy baratos por iteración (O(n))**, aceptando peores tasas de convergencia (O(1/ε) o incluso O(1/ε²) en el caso no diferenciable) que se compensan parcialmente con **aceleración** (Nesterov, FISTA: O(1/√ε)). El capítulo extiende además el marco teórico a funciones **no diferenciables** (subgradientes, regularización L1/LASSO para inducir dispersión) y a problemas **con restricciones** (métodos proyectados, Frank-Wolfe), sentando las bases para los Algoritmos de Punto Interior y los métodos de gran escala/descomposición que se tratan en capítulos posteriores del apunte.
