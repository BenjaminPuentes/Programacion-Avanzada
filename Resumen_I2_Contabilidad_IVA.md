# RESUMEN COMPLETO — ICS 2613 Contabilidad y Control de Gestión
## Interrogación 2: Contabilidad de Costos + Estado de Flujos de Efectivo

---

# PARTE 1: CONTABILIDAD DE COSTOS

---

## 1. Conceptos Fundamentales

### ¿Qué es un Costo?
Recursos sacrificados por la empresa para alcanzar un objetivo. Un costo es un **activo** hasta que se recibe su beneficio; en ese momento se convierte en **gasto**.

| Tipo | ¿Cuándo ocurre? | Dónde aparece |
|---|---|---|
| **Activo (costo no expirado)** | Cuando el beneficio se recibirá en el futuro | Balance (ESF) |
| **Gasto (costo expirado)** | Cuando el beneficio ya se recibió | Estado de Resultados |

### Regla clave: ¿Cuándo activar vs. gastar?
- **Se activa** si el costo fue incurrido para **obtener el producto** (compra o fabricación). El beneficio se recibirá cuando se venda.
- **Se gasta** si el costo es necesario para la **marcha de la empresa** (administración, ventas, finanzas), sin relación directa con la obtención del producto. Su beneficio se recibe en el mismo período.

---

## 2. Empresa Comercializadora vs. Manufacturera

### Empresa Comercializadora
- **Costos activables (inventario):** precio de compra, transporte, carga/descarga, derechos de internación, seguros de la mercadería.
- **Gastos del período:** arriendos de locales, sueldos administrativos, comisiones de vendedores, publicidad, intereses.

### Empresa Manufacturera
Separación en dos grandes grupos:

#### 1) Costos de Producción o Fabricación (activables → inventario)
Son los costos incurridos para **obtener el producto**. Se dividen en:

| Clasificación | Descripción | Ejemplos |
|---|---|---|
| **Materia Prima Directa (MPD)** | Materiales físicos identificables con el producto | Tela en una fábrica de ropa |
| **Mano de Obra Directa (MOD)** | Trabajo directamente aplicado al producto | Sueldos de operarios de línea |
| **Costos Indirectos de Fabricación (GIF/CIF)** | Costos de producción NO directamente identificables con una unidad | Arriendo fábrica, depreciación maquinaria, seguridad fábrica, MOI |

#### 2) Costos de No Producción (gastos del período)
Necesarios para el funcionamiento general de la empresa. **Nunca se activan.** Se registran como Gastos de Administración y Ventas (GAV):
- Sueldos personal administrativo
- Depreciación de activos no productivos (computador gerente, etc.)
- Comisiones de vendedores
- Publicidad y marketing
- Arriendos de oficinas/locales de venta
- Intereses financieros

> **Regla de oro:** Si el costo ocurre DENTRO de la fábrica y sirve para fabricar el producto → costo de producción. Si ocurre FUERA de la fábrica o sirve para vender/administrar → gasto del período.

---

## 3. Clasificación por Comportamiento: Fijos vs. Variables

| Tipo | Definición | Ejemplos |
|---|---|---|
| **Variable** | Cambia proporcionalmente con las unidades producidas/vendidas | MPD, MOD por unidad, comisiones por venta, energía de producción |
| **Fijo** | No cambia dentro de un rango de producción | Arriendo fábrica, depreciación en base al tiempo, sueldo gerente, seguridad |

> **¡Ojo!** No confundir directo/indirecto con fijo/variable. Un costo puede ser directo y fijo (ej: MOD con sueldo fijo) o indirecto y variable (ej: energía compartida entre productos).

**Clasificación cruzada de costos de producción:**
- MPD Variable → siempre activa
- MPD Fija → siempre activa
- MOD Variable → activa (costeo variable y absorción)
- MOD Fija → activa en absorción; **gasto en costeo variable**
- GIF Variable → activa en ambos sistemas
- GIF Fijo → activa en absorción; **gasto en costeo variable**

---

## 4. Sistemas de Costeo: Absorción vs. Variable

### Costeo por Absorción (Indirecto)
- **Obligatorio bajo IFRS** para estados financieros externos.
- Todos los costos de producción (variables Y fijos) se incorporan al costo del producto.
- Los costos fijos de producción se distribuyen entre las unidades producidas.
- **Costo unitario = MPD + MOD + GIF variables + GIF fijos / unidades producidas**

**Problema:** Si se produce más de lo que se vende, parte de los costos fijos queda en inventario (balance), lo que puede inflar el resultado e incentivar producir más solo para "diluir" los fijos.

### Costeo Variable (Directo)
- Solo para uso **interno** (contabilidad administrativa).
- Solo los costos **variables** de producción se activan en inventario.
- Los costos **fijos** de producción van directamente al Estado de Resultados como gasto del período.
- **Costo unitario = MPD variable + MOD variable + GIF variables**

**Ventaja:** El resultado NO depende de cuánto se produce, solo de cuánto se vende. Elimina el incentivo de sobre-producir.

### Estructura del EERR según cada sistema

**Costeo por Absorción:**
```
+ Ingresos por ventas
- Costo de ventas (MPD + MOD + GIF fijos y variables — solo de unidades vendidas)
= Margen Bruto
- Gastos de Administración y Ventas (fijos + variables)
= Resultado Operacional
```

**Costeo Variable:**
```
+ Ingresos por ventas
- Costo de ventas variable (solo CVu × unidades vendidas)
= Margen de Contribución
- Costos Fijos (producción + administración y ventas)
= Resultado Operacional
```

### Ejemplo comparativo (Juancho Aventuras SpA)
- Precio venta: $21.000/unidad
- CVu producción: $8.000 (MPD $5.000 + MOD $3.000)
- GAV variable: $2.000/unidad vendida
- CF producción: $1.500.000 / CF GAV: $450.000
- Mes 1: Producción 400 u, Ventas 300 u

| Concepto | Absorción | Variable |
|---|---|---|
| Costo fijo x unidad producida | $3.750 | No aplica |
| Inventario final (100 u) | $1.175.000 | $800.000 |
| Resultado Operacional | $1.725.000 | $1.350.000 |

La diferencia ($375.000) = costos fijos de fabricación que en absorción quedan activados en el inventario (100 u × $3.750).

> **Diferencia entre sistemas = CF unitario × (Inv. Final − Inv. Inicial)**

---

## 5. Costeo por Proceso y Unidades Equivalentes

Usado cuando la producción es **masiva y homogénea** (misma unidad en serie).

### Unidades Equivalentes
Cuando hay unidades en proceso al final del período, no se pueden contar igual que las terminadas. Se calcula cuántas unidades terminadas "equivalen" el trabajo incorporado.

**Fórmula:**
```
Unidades Equivalentes (UE) = Unidades terminadas × 100% + Unidades en proceso × % avance
```

**Importante:** El % de avance puede ser **diferente para cada insumo** (ej: MPD se incorpora al 100% al inicio, pero MOD se incorpora en forma continua).

**Ejemplo:**
- 100 unidades terminadas
- 50 unidades en proceso al 50% de avance
- MPD: incorporada al 100% al inicio → UE = 100 + 50×100% = 150
- MOD: continua → UE = 100 + 50×50% = 125

**Costo unitario por insumo = Costo total del insumo / Unidades Equivalentes**

---

## 6. Punto de Equilibrio

Nivel de ventas en que los Ingresos Totales = Costos Totales → Utilidad = 0.

### Fórmula base
```
Qe = CFT / (PV − CVu)
```
Donde:
- **CFT** = Costos Fijos Totales (producción + GAV)
- **PV** = Precio de Venta unitario
- **CVu** = Costo Variable unitario total (producción + venta)
- **(PV − CVu)** = Margen de Contribución Unitario (MCu)

### Con utilidad objetivo
```
Q = (CFT + Utilidad Operacional deseada) / MCu
```

### Con utilidad DESPUÉS de impuestos
```
Utilidad antes de impuestos = Utilidad neta / (1 − tasa impuesto)
Q = (CFT + Utilidad antes de impuestos) / MCu
```

### Punto de equilibrio en $ de ventas
```
PE en $ = CFT / (MCu/PV)    donde (MCu/PV) = Razón de contribución
```

### Ejemplos de cálculo
**Empresa de revistas:** CFT=$200.000, PV=$90, CVu=$50 → Qe = 200.000/40 = **5.000 unidades**

**Fábrica de zapatos:** CFT=$90.000.000, PV=$10.000, CVu=$5.000 → Qe = 90M/5.000 = **18.000 pares**

### Aplicaciones del punto de equilibrio
- Decidir precios de venta mínimos
- Evaluar impacto de cambios en costos o volumen
- Planificar utilidades
- Decidir expansión o contracción

### Supuestos del modelo
1. Precio de venta y CVu son constantes
2. CFT son constantes dentro del rango analizado
3. Todo lo producido se vende

---

## 7. Costos Indirectos de Fabricación (GIF/CIF)

Son costos de producción que NO pueden identificarse directamente con una unidad específica:
- **Materia Prima Indirecta (MPI):** materiales que no van físicamente en el producto (ej: lubricantes)
- **Mano de Obra Indirecta (MOI):** personal de producción no directamente en la línea (ej: supervisores)
- **Otros GIF:** arriendo fábrica, depreciación maquinaria, seguridad fábrica, energía compartida

> Si una empresa produce **un solo producto**, técnicamente no hay costos indirectos porque todos pueden identificarse con ese producto. En la práctica, igual se puede tener MOI u OGIF.

---

# PARTE 2: ESTADO DE FLUJOS DE EFECTIVO (EFE)

---

## 1. ¿Por qué existe el EFE?

- La utilidad contable no equivale a efectivo generado.
- Las empresas quiebran por **falta de efectivo**, no de utilidades.
- El EFE muestra las **fuentes y usos de efectivo** durante un período.

**Diferencia clave con el EERR:** El EERR usa base devengado (reconoce ingresos cuando se ganan y gastos cuando se incurren). El EFE usa base **caja** (solo movimientos reales de efectivo).

---

## 2. ¿Qué es "Efectivo" para el EFE? (NIC 7)
- Caja y banco (cuenta corriente, cuenta vista)
- Vale vista
- Activos Equivalentes al Efectivo (AEC): inversiones de **menos de 90 días**, fácilmente convertibles, con riesgo insignificante → depósitos a plazo ≤90 días, fondos mutuos líquidos.

> Un depósito a plazo de **30 días** es efectivo equivalente. Uno de 6 meses, NO.

---

## 3. Las Tres Secciones del EFE

### A) Operación
Actividades relacionadas con la venta de bienes y servicios del **giro** del negocio.

**Entradas (fuentes):**
- Cobros a clientes por ventas al contado
- Cobros de cuentas por cobrar
- Cobros de anticipos de clientes (IPPA recibidos)

**Salidas (usos):**
- Pagos a proveedores por compras
- Pagos de sueldos y remuneraciones
- Pagos de seguros pagados por anticipado (SPPA)
- Pago de impuestos a la renta (cuando se pagan, no cuando se devengan)
- Pago de intereses (en algunos casos)

### B) Inversión
Adquisición y venta de **activos no corrientes** (largo plazo) no relacionados directamente con el giro.

**Entradas:**
- Venta de PP&E (propiedades, plantas y equipos) — se usa el **precio de venta**, no el valor libro
- Venta de activos intangibles
- Venta de inversiones financieras de largo plazo

**Salidas:**
- Compra de PP&E
- Compra de activos intangibles
- Compra de inversiones financieras de largo plazo

### C) Financiamiento
Cambios en el **patrimonio** y **pasivos financieros** (deudas con bancos, bonos).

**Entradas:**
- Aumento de capital en efectivo
- Obtención de préstamos bancarios

**Salidas:**
- Pago de préstamos (capital, no intereses)
- Pago de dividendos (solo cuando se PAGAN, no cuando se declaran)
- Pago de intereses (cuando son de financiamiento)

---

## 4. Regla de Clasificación: ¿Operación, Inversión o Financiamiento?

| Transacción | Sección |
|---|---|
| Cobro a cliente por venta | Operación |
| Pago a proveedor | Operación |
| Pago de sueldos | Operación |
| Pago de arriendo del local | Operación |
| Pago de seguro de incendio | Operación |
| Recibo de anticipo de cliente (IPPA) | Operación |
| Pago de impuesto a la renta | Operación |
| Compra de vehículo / maquinaria / edificio | Inversión |
| Venta de activo fijo (monto recibido en $) | Inversión |
| Compra de terreno | Inversión |
| Compra de activo intangible (marca, patente) | Inversión |
| Aumento de capital en efectivo | Financiamiento |
| Obtención préstamo bancario | Financiamiento |
| Pago de préstamo bancario (capital) | Financiamiento |
| Pago de dividendos | Financiamiento |
| Pago de intereses financieros | Operación o Financiamiento* |

\* Los intereses pagados generalmente van en Operación bajo IFRS, pero el curso los acepta en Financiamiento cuando corresponden a deuda financiera.

---

## 5. Transacciones que NO van en el EFE (no hay movimiento de efectivo)

Las siguientes transacciones **no afectan el EFE** (aunque afectan EERR o Balance):
- Depreciación (gasto sin salida de efectivo)
- Estimación de deudores incobrables / Gasto por PDI
- Reconocimiento de seguro devengado (gasto por SPPA)
- Interés devengado pero no pagado (Interés × pagar)
- Impuesto a la renta devengado pero no pagado
- Sueldos devengados pero no pagados
- Declaración de dividendos (sin pago)
- Compra de terreno con crédito del vendedor (no hay efectivo)
- Venta a crédito (sin cobro)
- Aumento de capital con bienes (no efectivo)

> **Regla práctica:** Busca en los asientos contables las transacciones que involucran la cuenta **Efectivo/Banco/Caja**. Esas son las que van al EFE.

---

## 6. Casos Especiales Recurrentes en Pruebas

### Venta de activo fijo
Se registra en **Inversión** por el monto de **efectivo recibido** (precio de venta), NO por el valor libro.

**Asiento:**
```
Efectivo (precio venta)                  XX
Depreciación Acumulada                   XX
    PP&E (costo histórico)                    XX
    Utilidad/Pérdida en venta (diferencia)    XX  ← va al EERR, no al EFE
```

**En el EFE:** Solo va la entrada de efectivo recibida → Inversión.

**En el EERR:** Solo va la utilidad o pérdida por la venta (no el efectivo).

### Aumento de capital
- Si es **en efectivo** → Financiamiento (entrada)
- Si es **con un depósito a plazo** de hasta 90 días → también es efectivo equivalente → Financiamiento (entrada)
- Si es **con un bien** → no va al EFE

### Pago de seguros (SPPA)
- El pago en efectivo → **Operación** (salida)
- El gasto devengado mensual → **no va al EFE**

### Dividendos
- **Declaración:** afecta Patrimonio (baja Utilidades Retenidas, sube Dividendos × Pagar). **No va al EFE.**
- **Pago:** afecta el EFE → **Financiamiento** (salida). **No afecta Patrimonio** (baja el pasivo).

### Pago anticipado recibido (IPPA / anticipo de clientes)
- **Recepción de efectivo** → Operación (entrada). Crea un pasivo (IPPA).
- **Entrega del bien** → No mueve efectivo. Se reconoce ingreso y se cancela el pasivo.

---

## 7. Estructura del EFE (Método Directo)

```
ESTADO DE FLUJOS DE EFECTIVO
Período terminado el [fecha]

ACTIVIDADES DE OPERACIÓN
  Cobros de clientes                         +XX
  Pagos a proveedores                        -XX
  Pago de sueldos                            -XX
  Pago de seguros                            -XX
  Pago de impuestos                          -XX
  Otros pagos operacionales                  -XX
TOTAL OPERACIÓN                           +/- XX

ACTIVIDADES DE INVERSIÓN
  Compra de PP&E                             -XX
  Venta de PP&E                              +XX
  Compra de activos intangibles              -XX
TOTAL INVERSIÓN                           +/- XX

ACTIVIDADES DE FINANCIAMIENTO
  Obtención de préstamos                     +XX
  Pago de préstamos                          -XX
  Aumento de capital                         +XX
  Pago de dividendos                         -XX
TOTAL FINANCIAMIENTO                      +/- XX

CAMBIO NETO EN EFECTIVO                   +/- XX
EFECTIVO INICIAL                             +XX
EFECTIVO FINAL                               +XX
```

> **Verificación:** Efectivo Final = Efectivo Inicial + Cambio Neto. Debe coincidir con la cuenta de efectivo en el Balance Final.

---

## 8. Cómo Construir el EFE Desde los Asientos Contables

**Paso 1:** Identifica en cada asiento si aparece la cuenta **Efectivo/Banco/Caja**.
- Si está en el **Debe** → entrada de efectivo (positivo)
- Si está en el **Haber** → salida de efectivo (negativo)

**Paso 2:** Clasifica cada movimiento de efectivo:
- ¿Relacionado con el giro del negocio (venta de productos, pago de gastos operativos)? → **Operación**
- ¿Relacionado con activos de largo plazo? → **Inversión**
- ¿Relacionado con deuda financiera o patrimonio? → **Financiamiento**

**Paso 3:** Agrupa los movimientos por categoría y suma.

**Paso 4:** Presenta el cuadro con el efectivo inicial y final.

---

## 9. Cómo Comentar el EFE (Pregunta Teórica)

Un buen comentario menciona:
1. **El cambio total en efectivo** y si fue positivo o negativo (con porcentaje si es posible).
2. **Qué causó el cambio:** La operación ¿generó o consumió efectivo? La inversión ¿fue importante? El financiamiento ¿compensó?
3. **Alerta o tranquilidad:** ¿Es preocupante la situación? ¿Es sostenible?

**Ejemplo de comentario bien evaluado:**
> "El efectivo disminuyó en $55.700.000 (54%). La operación consumió $25.700.000 y la inversión significó usar efectivo por $42.000.000. El aumento de capital ayudó a contener la disminución, pero se debe estar atento a la situación de efectivo."

---

# PARTE 3: IVA — IMPUESTO AL VALOR AGREGADO

---

## 1. Concepto General

- El IVA es un impuesto a los **consumidores finales**, NO a las empresas.
- En Chile es del **19%** y lo recauda el SII.
- Las empresas actúan como **intermediarias**: cobran el IVA a sus clientes y lo entregan al Estado, descontando el IVA que ellas mismas pagaron al comprar.

### ¿Por qué lo pagan los consumidores?
Cada empresa paga IVA solo sobre el **valor que ella agrega**. El consumidor final no puede descontar nada, por lo que absorbe el total del impuesto acumulado en la cadena.

**Ejemplo de la cadena de valor:**

| Actor | Precio neto | IVA Débito | IVA Crédito | Paga al SII |
|---|---|---|---|---|
| Campo de Trigo | $30.000 | $5.700 | $0 | $5.700 |
| Fábrica de Harina | $70.000 | $13.300 | $5.700 | $7.600 |
| Panadería | $120.000 | $22.800 | $13.300 | $9.500 |
| **Consumidor Final** | — | — | — | **$22.800 (total)** |

La suma de lo que cada empresa paga al SII ($5.700 + $7.600 + $9.500 = $22.800) es exactamente igual al IVA que paga el consumidor final sobre el precio final.

---

## 2. Las Dos Cuentas del IVA

| Cuenta | Cuándo se usa | Naturaleza | Dónde aparece |
|---|---|---|---|
| **IVA Crédito Fiscal** | Al **comprar** bienes o servicios | Activo corriente (saldo deudor) | Balance — "IVA por recuperar" |
| **IVA Débito Fiscal** | Al **vender** bienes o servicios | Pasivo corriente (saldo acreedor) | Balance — "IVA por pagar" |

---

## 3. Conceptos de Precio

- **Valor Neto:** precio **sin** IVA → es el ingreso que registra la empresa en su EERR
- **Valor Bruto:** precio **con** IVA → es lo que paga el comprador en efectivo

> El EERR siempre muestra montos **netos** (sin IVA). El IVA nunca afecta el resultado.

---

## 4. Asientos Contables

### Al comprar (ejemplo: $100 neto + IVA 19% = $119 bruto)
```
Existencias (Activo)        $100
IVA Crédito Fiscal (Activo)  $19
    Caja / Banco (Activo)         $119
```

### Al vender (ejemplo: $150 neto + IVA 19% = $178,5 bruto)
```
Caja / Banco (Activo)       $178,5
    Ingreso por Venta (Resultado)   $150
    IVA Débito Fiscal (Pasivo)       $28,5
```

### Al cierre del período: Regularización del IVA
Se comparan IVA Débito e IVA Crédito:

**Caso 1 — IVA Crédito > IVA Débito** (compré más de lo que vendí):
El Estado le debe a la empresa. El saldo queda como **IVA Crédito** para el mes siguiente.
```
IVA Débito Fiscal    $XX
    IVA Crédito Fiscal    $XX   (solo la parte que compensa)
```
El remanente de IVA Crédito queda como activo corriente en el Balance.

**Caso 2 — IVA Débito > IVA Crédito** (vendí más de lo que compré):
La empresa le debe al Estado. Se genera un pasivo que se paga el mes siguiente.
```
IVA Débito Fiscal    $XX
    IVA Crédito Fiscal    $XX   (todo el crédito disponible)
    IVA por Pagar         $XX   (diferencia = lo que se le debe al SII)
```

### Al pagar el IVA al SII (entre el 1 y el 20 del mes siguiente)
```
IVA por Pagar (Pasivo)    $XX
    Caja / Banco (Activo)      $XX
```

---

## 5. Declaración de IVA al SII

- Se declara **mensualmente**
- Facturadores electrónicos: entre el **1 y el 20** del mes siguiente
- Resto de empresas: entre el **1 y el 12** del mes siguiente

---

## 6. Efecto en los Estados Financieros

| Estado | Efecto del IVA |
|---|---|
| **EERR** | **Ninguno.** Los ingresos y costos se registran siempre en valores **netos** (sin IVA) |
| **Balance (ESF)** | IVA Crédito → Activo corriente / IVA Débito o por Pagar → Pasivo corriente. Las CxC incluyen IVA si la venta fue a crédito; las CxP incluyen IVA si la compra fue a crédito |
| **EFE** | Los flujos de efectivo se registran por el valor **bruto** (con IVA), ya que es lo que realmente entró o salió de caja. El IVA pagado al SII va en Operación |

---

## 7. Ejemplo Completo (Flechita Pabajo S.A.)

**Enero:** Compra 50 unidades a $5.000 neto (+IVA $950). Vende 10 unidades a $2.000 neto (+IVA $380).

- Regularización: IVA Crédito ($950) > IVA Débito ($380) → saldo crédito de $570 pasa al mes siguiente.
- Balance: IVA Crédito $570 en activo corriente. No se paga nada al SII.

**Febrero:** Compra 20 unidades a $2.000 neto (+IVA $380). Vende 40 unidades a $9.000 neto (+IVA $1.710).

- IVA Crédito acumulado: $570 (enero) + $380 (febrero) = $950
- Regularización: IVA Débito ($1.710) > IVA Crédito ($950) → IVA por Pagar = $760
- Se paga $760 al SII en marzo.

**EERR acumulado (2 meses):**
```
Ingresos por venta   $11.000   (neto, sin IVA)
Costo por venta      ($5.000)
Resultado             $6.000
```
El IVA no aparece en ninguna parte del EERR.

---

## 8. Puntos Clave para la Prueba

- El IVA **nunca afecta el Estado de Resultados**. Ingresos y costos siempre en valores netos.
- El IVA Crédito es un **activo** (el Estado le debe a la empresa).
- El IVA Débito es un **pasivo** (la empresa le debe al Estado).
- Las CxC y CxP incluyen el IVA si la operación fue a crédito (el monto bruto es la deuda real).
- En el EFE, los cobros y pagos se registran por el monto **bruto** (con IVA).
- Si en el enunciado dice "suponga que no hay IVA", los precios dados son netos y no se aplica el 19%.

---

# PARTE 4: TEMAS COMPLEMENTARIOS (Área II de Pruebas)

---

## 1. Provisión por Deudores Incobrables (PDI / EDI)

La PDI es una cuenta **contrarectificadora de activo** que reduce el valor de las CxC en el Balance.

### ¿Cómo funciona?
1. **Estimación inicial:** Se crea la PDI (gasto) para anticipar futuras pérdidas.
2. **Declaración definitiva de incobrable:** Se elimina la CxC y se usa la PDI existente. **No genera nuevo gasto.**
3. **Nueva estimación:** Se ajusta la PDI al monto que corresponda. La diferencia es el nuevo gasto.

### Cuenta T de la PDI:
```
            PDI (EDI)
Incobrables  |  Saldo inicial
declarados   |  Nueva estimación (Gasto × PDI)
             |
             |  Saldo final
```

### Cálculo del efecto en EERR:
**Solo el Gasto × PDI de la nueva estimación afecta el EERR del período.**

Los incobrables declarados definitivamente NO afectan el resultado (ya fue provisionado en períodos anteriores).

**Ejemplo (prueba 2024-2):**
- PDI inicial: $10.000
- Incobrables declarados: $7.300 → salen de la PDI (no afectan EERR)
- Nueva estimación: $8.300 → este es el Gasto × PDI (afecta EERR)
- PDI final: $10.000 − $7.300 + $8.300 = $11.000

### Política porcentual:
Si la empresa aplica un % sobre el saldo de CxC brutas:
- Gasto = PDI objetivo − PDI actual (antes del ajuste)
- Si PDI objetivo > PDI actual → gasto positivo (aumenta pérdida)
- Si PDI objetivo < PDI actual → ingreso/reversión (aumenta ganancia)

---

## 2. Descuento de Deudas (Nota de Crédito / Condonación Parcial)

Cuando un cliente no puede pagar el total y la empresa acepta menos:

**Asiento:**
```
Banco/Efectivo         (monto recibido)
Gasto por Descuento    (diferencia)
    Cuentas × Cobrar       (monto total original)
```

**Efecto en EERR:** El Gasto por Descuento reduce el resultado del período.
**Ejemplo:** Deuda $556.000, paga $500.000 → Gasto por Descuento = $56.000.

---

## 3. Preguntas de Comento: Verdadero o Falso

Estas preguntas evalúan si entiendes la lógica contable. Hay que:
1. Decir explícitamente **Verdadero o Falso**
2. Argumentar **por qué** con precisión contable

### Casos típicos recurrentes:

**"La depreciación de una máquina de producción afecta el EFE"**
→ **DEPENDE.** Si la empresa es manufacturera y la máquina está en producción, la depreciación se **activa** (va a inventario), NO al EERR ni al EFE. Si ya se vendieron las unidades, entonces llegará al EERR como parte del costo de ventas, pero igual **nunca va al EFE** (la depreciación nunca es efectivo). → **Falso** que afecte el EFE directamente.

**"La venta al contado de un activo fijo a su valor libro genera un flujo de inversión igual al costo histórico menos la depreciación acumulada"**
→ **Verdadero.** Precio de venta = valor libro neto = costo histórico − depreciación acumulada. Ese monto entra como flujo positivo en Inversión.

**"El pago de dividendos disminuye el Patrimonio"**
→ **Falso.** El Patrimonio disminuye cuando se *declaran* los dividendos (bajan Utilidades Retenidas). Al *pagar*, lo que disminuye es el **pasivo** Dividendos × Pagar. El Patrimonio ya bajó al declarar.

**"Las comisiones de venta variables se incluyen en el costo del producto"**
→ **Falso.** Las comisiones de venta son costos de **no producción** (GAV), independientemente de si son fijas o variables. Nunca se activan en el inventario.

**"Los GIF serán iguales bajo ambos sistemas de costeo si son variables"**
→ **Verdadero para GIF variables:** En ambos sistemas (absorción y variable) los GIF variables se activan como parte del producto. Si son **fijos**, la diferencia es que en absorción se activan y en variable son gasto del período.

**"Un EERR positivo garantiza flujo positivo en Operación"**
→ **Falso.** Son conceptos distintos. Una empresa puede tener utilidades y consumir efectivo en operaciones (ej: ventas a crédito, compra masiva de inventario). El EFE es base caja; el EERR es base devengado.

**"Un pago anticipado recibido genera Ingreso por Ventas ese día"**
→ **Falso.** Se reconoce un **pasivo** (IPPA o Anticipo de Clientes). El ingreso se reconoce cuando se entrega el bien/servicio.

**"El pago de arriendo de un local de ventas va en la sección Financiamiento del EFE"**
→ **Falso.** Va en **Operación** porque el arriendo del local de ventas es parte de la actividad operacional de la empresa.

---

## 4. Valores Negociables e Inversión en Asociadas (IER)

### Valores Negociables (VN)
- **Para Negociar (VPN):** ajuste a valor de mercado → **ganancia/pérdida en EERR**
- **Disponibles para Venta (DPV):** ajuste a valor de mercado → **Otras Reservas en Patrimonio** (no afecta EERR hasta venta)

### Inversión en Asociadas (IER / Método de Participación)
Cuando la empresa tiene 20-50% de otra empresa:
- Al ganar utilidades la asociada: `IER (débito) / Ganancia IER (crédito)` — afecta EERR
- Al declarar dividendos la asociada: `Dividendos × Cobrar (débito) / IER (crédito)` — no afecta EERR
- Al pagar dividendos la asociada: `Efectivo (débito) / Dividendos × Cobrar (crédito)` — afecta EFE (Operación)
- El valor de mercado de la asociada **no se ajusta** (se usa valor libro con método de participación)

---

# PARTE 5: GUÍA PARA RESOLVER EJERCICIOS

---

## Checklist para el EFE

1. **Identificar el efectivo inicial** (suma de Caja + Banco + depósitos ≤90 días al inicio del período)
2. **Revisar cada transacción** y marcar si involucra efectivo
3. **Clasificar** en O/I/F
4. **Sumar por sección**
5. **Calcular cambio neto** (O + I + F)
6. **Sumar al efectivo inicial** → debe dar el efectivo en el Balance Final

## Checklist para el EERR (Costeo Variable)

1. Ingresos = PV × unidades vendidas
2. Costo variable = CVu × unidades vendidas (solo producción, no GAV)
3. Margen de Contribución = Ingresos − Costo variable
4. Costos fijos = todos los CF (producción + GAV)
5. Utilidad Operacional = MC − CF totales

## Checklist para el Punto de Equilibrio

1. Identificar PV, CVu total (producción + venta), CFT
2. MCu = PV − CVu
3. Qe = CFT / MCu
4. Si piden utilidad objetivo: Q = (CFT + U) / MCu
5. Si la utilidad es DESPUÉS de impuestos: primero despejar U antes de impuestos = U neta / (1 − t)

---

# RESUMEN DE FÓRMULAS CLAVE

| Fórmula | Descripción |
|---|---|
| `Qe = CFT / (PV − CVu)` | Punto de equilibrio básico |
| `Q = (CFT + U_operacional) / MCu` | Con utilidad operacional objetivo |
| `Q = (CFT + U_neta/(1−t)) / MCu` | Con utilidad neta después de impuestos |
| `MCu = PV − CVu` | Margen de contribución unitario |
| `UE = Terminadas × 100% + En proceso × %avance` | Unidades equivalentes |
| `Costo unitario = Costo total del insumo / UE` | Costo por unidad equivalente |
| `Efectivo final = Efectivo inicial + ΔO + ΔI + ΔF` | Verificación EFE |
| `Diferencia Absorción vs Variable = CF unitario × (Inv. Final − Inv. Inicial)` | Diferencia entre sistemas |

---

# ERRORES FRECUENTES A EVITAR

1. **Poner la depreciación en el EFE** → nunca va (es gasto sin salida de efectivo)
2. **Poner el gasto por PDI en el EFE** → nunca va
3. **Poner la declaración de dividendos en el EFE** → el EFE solo registra el PAGO
4. **Poner el interés devengado (no pagado) en el EFE** → solo va cuando se paga
5. **Incluir comisiones de venta en el costo del producto** → siempre son GAV
6. **Olvidar que en costeo variable los CF de producción son gasto del período** (no se activan)
7. **En costeo por absorción, dividir CF por unidades producidas** (no vendidas)
8. **En la venta de PP&E, poner el valor libro en el EFE** → se pone el precio de venta (efectivo recibido)
9. **Calcular el punto de equilibrio sin incluir todos los CVu** (olvidar comisiones variables o GAV variable)
10. **Confundir el aumento de capital con bien (no efectivo)** → no va en el EFE

---

*Resumen elaborado a partir de CLASES_I2.pdf e Interrogaciones 2 de los semestres 2023-1, 2023-2, 2024-1 y 2024-2 del curso ICS 2613, Pontificia Universidad Católica de Chile.*
