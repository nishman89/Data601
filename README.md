[![Python CI with pytest](https://github.com/nishman89/Data601/actions/workflows/python-package.yml/badge.svg)](https://github.com/nishman89/Data601/actions/workflows/python-package.yml)

# H1 Headings

## H2 Headings

### H3 Headings

###### H6 Headings

## Stylings 

*This is italics*

_This is also italics_

__This is bold__

**This is also bold**

## Comments

> NOTES
>
> Remember to add this to the document
>
> > And also pick up some granola on the way
> > > Though check protein content

## Lists 

- this
- that 
- the other

* first
* second 
* third

<br>

1. One
1. Two
1. Three
   - 3

## Links


### Pictures
<!-- 
![my-pic](./assets/profilepic.jpg)

![online-pics](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwf_wGhh84q5sJd-fLlF6KPOnC4IZhouNRPw&s) -->


### External links

This is my [markdown cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)


### Link to document headers

- [h2 headings](#h2-headings)
- [Links](#links)
- [Lists](#lists)

## GitHub Flavored Markdown

```csharp
public static Main()
{
    Console.WriteLine("Hello, World!");
}
```

```python
list1 = [1,2,3,4]
```

```sql
SELECT * FROM Customers
```


## Tasks Lists

- [ ] This is a tasks
- [X] This is a completed task 

Name | Street | Town
-----|--------|-----
Nish|Python St| Oxford
Nash|C# St| Brum


## Mermaid

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses

```


```mermaid
quadrantChart
    title Pokémon: Popularity vs Battle Power
    x-axis Low Battle Power --> High Battle Power
    y-axis Low Popularity --> High Popularity
    quadrant-1 Fan Favorites & Powerhouses
    quadrant-2 Beloved but Underrated
    quadrant-3 Forgotten & Weak
    quadrant-4 Strong but Overlooked

    Mewtwo: [0.95, 0.90]
    Pikachu: [0.35, 0.99]
    Charizard: [0.85, 0.95]
    Eevee: [0.25, 0.88]
    Gengar: [0.72, 0.85]
    Dragonite: [0.80, 0.78]
    Snorlax: [0.55, 0.82]
    Rayquaza: [0.92, 0.75]
    Lucario: [0.78, 0.80]
    Garchomp: [0.90, 0.65]
    Magikarp: [0.05, 0.72]
    Jigglypuff: [0.18, 0.70]
    Togekiss: [0.65, 0.55]
    Alakazam: [0.82, 0.50]
    Scizor: [0.76, 0.48]
    Aegislash: [0.84, 0.40]
    Caterpie: [0.08, 0.30]
    Rattata: [0.12, 0.18]
    Beedrill: [0.38, 0.22]
    Dunsparce: [0.20, 0.25]
```
