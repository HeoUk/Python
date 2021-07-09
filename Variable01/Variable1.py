#pycham인 경우 File->Serrings->Editor->File Encodings인코딩 설정
#변경시 아래 인코딩지정 불필요
#coding:utf-8
#변수 선언 방법1]변수명 = 데이터
a=10
print(a,type(a),sep='\n')#type(변수):자료형 반환 <class 'int'>
#변수 선언 방법2]변수명1, 변수명2, 변수명3,.. = 반복가능한 객체(이터레이터)
#이터레이터의 요소를 여러 변수에 나눠 담는 것을 언패킹(unpacking) 또는 구조분해(destructuring)라고 한다.
#변수명1, 변수명2, 변수명3 = 데이타1, 데이타2, 데이타3 혹은 (데이타1, 데이타2, 데이타3)
#특히 대입문에서는  패킹과 언패킹을 수행할 때 괄호를 생략하는 경우가 많다
a,b,c = '파이썬',"10",20#a,b,c = ('파이썬',"10",20)
print('a의 값:%s a의 자료형:%s' % (a,type(a)))
print('b의 값:{} b의 자료형:{}'.format(b,type(b)))
print('c의 값:',c,' c의 자료형:',type(c),sep="")
#변수 선언 방법3]변수명 = 반복가능한 객체(이터레이터)
#여러 개의 데이터를 이터레이터를 이용해 하나의 변수에 묶어 담는 것을 패킹(packing)
#변수명 = 데이타1, 데이타2, 데이타3 혹은 (데이타1, 데이타2, 데이타3)
d=10,'20','파이썬'#int,str,str객체를 튜플로 묶어서(패킹) 변수 d에 저장
print('d의 값:',d,' d의 자료형:',type(d),sep="")
#변수 선언 방법4]변수명1 = None
#z#NameError: name 'z' is not defined
z=None
print('z의 값:',z,' z의 자료형:',type(z),sep="")#<class 'NoneType'>
x,y=10,20
print('x=',x,' y=',y,sep='')
print('[x 와 y값 치환]')
y,x=10,20
print('x=',x,' y=',y,sep='')
print('[키워드 목록]')
import keyword
print(keyword.kwlist)
#else = 10#SyntaxError: invalid syntax
#변수 삭제
del x#혹은 del(x)
#print(x)#삭제후 아래 에러 발생 NameError: name 'x' is not defined
