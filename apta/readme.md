this is an apta plugin for templ8.py. it's very epic.

apta is an ascii phonetic transcription system invented by the conlang critic discord server.

(this file is easiest to view when actually rendered!)

# conversions

## consonants

| |bilabial|labiodental|dental|alveolar|postalveolar|retroflex|palatal|velar|uvular|pharyngeal|glottal|\_palatal|\_velar|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|nasal|`m`|`m;`||`n`||`n;`|`J`|`N`|`N;`|
|stop|`p b`|||`t d`||`t; d;`|`c F`|`k g` (`\g`)|`q g;`|`?;`|`?`|
|fricative|`P B`|`f v`|`T D`|`s z`|`S Z`|`s; z;`|`C j;` (`S; Z;`)|`x G`|`X K`|`% Q`|`h H`|
|approximant||`V`||`R`||`R;`|`j`|`M;`||||`y;`|`w; w`|
|tap||`v;`||`4`||`r;`|
|trill|`B;`|||`r`|||||`K;`|`H; Q;`|
|lateral fricative||||`$ $;`|
|lateral approximant||||`l`||`l;`|`5`|`L;`|||||`L`|
|lateral tap||||`4;`|

implosives are formed as *stop*`<`, i.e. `p< b< t< d< t;< d;< c< F< k< g< q< g;<`

clicks are `0; |; ! =; #;` → `ʘ ǀ ǃ ǂ ǁ`

apta also includes symbols for nonstandard/extipa consonants:

|category|symbols|apta|
|:-:|:-|:-|
|nasals|ȵ 𝼇 ƞ|`n\| N;\| N\|`|
|stops|ȹ ȸ ȶ ȡ 𝼃 𝼁 ꞯ 𝼂|`p\| b\| t\| d\| k;\| g;\| Q\| g\|`|
|fricatives|σ ƍ ƪ ƺ ʆ ʓ ʩ 𝼀|`s;\| z;\| S;\| Z;\| S\| Z\| fN}; fN};\|`|
|laterals|ꞎ 𝼅 𝼆 𝼄 ʪ ʫ ȴ|`$\| $;\| 5\| L;\| ls}; lz}; l\|`|
|approximants|ϐ δ ɉ|`B\| D\| j\|`|
|taps|ɼ ⱳ 𝼈|`r\| w\| 4;\|`|
|clicks|𝼊|`!-R`|
|clicks2|ʇ ʗ 𝼋 ʖ|`T\| c\| F\| ?\|` (nasalized versions use `;\|`)|
|clicks3|ɋ ψ ʞ 𝼐|`q\| P\| k\| K\|`|
|percussives|ʬ ʭ ¡|`ww}; dd}; !\|`|

## vowels

| | front | mid | back |
|:-:|:-:|:-:|:-:|
|close|`i y`|`1 W`|`M u`|
||`I Y`|`I; U;`|`M\| U`|
||`e 0`|`e; o;`|`7 o`|
|mid|`e\|`|`@`|`7\| o\|`
||`E 9`|`3 O;`|`2 O`|
||`&`*|`6`|	
|open|`a 9;`*|`a\|`*|`A 8`|

* Big Phonology refuses to accept that /a/ is central. fuck them

## diacritics

you really think i want to document these?

### a note on tiebars

tiebars in apta are `}`/`-}`. unfortunately, due to the way the plugin works, you have to place the tiebar *between* the things being connected:

> `t$}` → `t}$` (outputs `t͡ɬ`)

this does not hold true of the joined affricates (`tS};` outputs `ʧ`)
