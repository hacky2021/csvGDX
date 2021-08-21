# csvGDX이란?
csv 파일을 파이썬에서 편집할수 있도록 하는 모듈
***
# csvGDX사용법
## 1. 파일 불러오기
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 입력 형식)
</code>
</pre>
### 1-1. 입력 형식
1:셀을 수정하거나 불러올때 행과 열을 엑셀과 같게 불러옵니다.
<pre>
<code>
from csvGDX import *
f = copen(파일 경로, 1)
f.setCell("A2","123")
</code>
</pre>
2:숫자로 불러옴니다.
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
