# csvGDX이란?
csv 파일을 파이썬 에서 편집할 수 있도록 하는 모듈입니다.
***
# csvGDX사용법
## 1. 파일 불러오기

<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
</code>
</pre>

## 1-1. 입력 형식
1:셀을 수정하거나 불러올 때 행과 열을 엑셀과 같게 불러옵니다.
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 1)
f.setCell("A2","123")
</code>
</pre>

2:숫자로 불러옵니다.
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 1)
f.setCell("0:1","123")
</code>
</pre>

## 2. 셀 수정
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.setCell(셀 위치, 값)
</code>
</pre>

## 3. 셀 불러오기
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.getCell(셀 위치)
</code>
</pre>

## 4. 셀 더하기
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.addCell(더할 셀 위치1, 더할 셀 위치2, 값을 저장할 셀 위치)
</code>
</pre>

## 5. 셀 빼기
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.subCell(뺄 셀 위치1, 뺄 셀 위치2, 값을 저장할 셀 위치)
</code>
</pre>

## 6. 셀 곱하기
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.mulCell(곱할 셀 위치1, 곱할 셀 위치2, 값을 저장할 셀 위치)
</code>
</pre>

## 7. 셀 나누기
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.shrCell(나눌 셀 위치1, 나눌 셀 위치2, 값을 저장할 셀 위치)
</code>
</pre>

## 8. 저장
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
f.save()
</code>
</pre>
