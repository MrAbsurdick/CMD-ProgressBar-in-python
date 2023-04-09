
# Progress Bar

Adds a custom development bar, with the ability to specify the maximum value, line size and the ability to specify no limit

## Usage
### NO-LIMIT = FALSE
```python
Bar = AbsProgressBar(max_value=100, size_line=20, no_limit=False)
Bar.display()
```
Console: ░░░░░░░░░░░░░░░░░░░░ [0/100]

```python
Bar.update(50)
Bar.display()
```
Console: ██████████░░░░░░░░░░ [50/100]

```python
Bar.update(-25)
Bar.display()
```
Console: █████░░░░░░░░░░░░░░░ [25/100]

---

### NO-LIMIT = TRUE

```python
Bar = AbsProgressBar(max_value=100, size_line=20, no_limit=False)
Bar.display()
```
Console: ░░░░░░░░░░░░░░░░░░░░ [0/100]

```python
Bar.update(150)
Bar.display()
```
Console: ████████████████████ [150/100]

```python
Bar.update(-200)
Bar.display()
```
Console: ░░░░░░░░░░░░░░░░░░░░ [-50/100]
