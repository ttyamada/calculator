import streamlit as st
import numpy as np

st.title("calculator")

TAU=(1+np.sqrt(5))/2.0

# 入力フィールド
st.markdown("""
val1 = (a1 + TAU * b1) / c1
""")
a1 = st.number_input("a1", value=0, step=1)
b1 = st.number_input("b1", value=0, step=1)
c1 = st.number_input("c1", value=1, step=1)
st.markdown("""
val2 = (a2 + TAU * b2) / c2
""")
a2 = st.number_input("a2", value=0, step=1)
b2 = st.number_input("b2", value=0, step=1)
c2 = st.number_input("c2", value=1, step=1)

# 演算の選択
operation = st.selectbox("select", ["addition", "subtraction", "multiplication", "division"])

def add(a,b):
    """
    # summation (a+b) in TAU-style
    
    Parameters
    ----------
    a: array
        value in TAU-style
    b: array
        value in TAU-style
    
    Returns
    -------
    array
    """
    c1=a[0]*b[2]+b[0]*a[2]
    c2=a[1]*b[2]+b[1]*a[2]
    c3=a[2]*b[2]
    x=np.array([c1,c2,c3],dtype=np.int64)
    g=np.gcd.reduce(x)
    c1=c1/g
    c2=c2/g
    c3=c3/g
    if c3<0:
        return np.array([int(-c1),int(-c2),int(-c3)])
    elif c1==0 and c2==0:
        return np.array([0,0,1])
    else:
        return np.array([int(c1),int(c2),int(c3)])

def mul(a,b):
    """
    # multiplication (a*b) in TAU-style
    
    Parameters
    ----------
    a: array
        value in TAU-style
    b: array
        value in TAU-style
    
    Returns
    -------
    array
    """
    c1=a[0]*b[0]+a[1]*b[1]
    c2=a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
    c3=a[2]*b[2]
    x=np.array([c1,c2,c3],dtype=np.int64)
    g=np.gcd.reduce(x)
    c1=c1/g
    c2=c2/g
    c3=c3/g
    if c3<0:
        return np.array([int(-c1),int(-c2),int(-c3)])
    elif c1==0 and c2==0:
        return np.array([0,0,1])
    else:
        return np.array([int(c1),int(c2),int(c3)])

def sub(a,b):
    """
    # subtraction (a/b) in TAU-style
    
    Parameters
    ----------
    a: array
        value in TAU-style
    b: array
        value in TAU-style
    
    Returns
    -------
    array
    """
    c=np.array([-1,0,1],dtype=np.int64)
    b=mul(c,b)
    return add(a,b)

def div(a,b):
    """
    # division (a/b) in TAU-style
    
    Parameters
    ----------
    a: array
        value in TAU-style
    b: array
        value in TAU-style
    
    Returns
    -------
    array
    """
    if np.all(b[:2]==0):
        print('ERROR_1:division error')
        return 
    else:
        if np.all(a[:2]==0):
            return np.array([0,0,1],dtype=np.int64)
        else:
            if b[1]!=0:
                if b[0]!=0:
                    c1=(a[0]*b[0] + a[0]*b[1] - a[1]*b[1])*b[2]
                    c2=(a[1]*b[0] - a[0]*b[1]            )*b[2]
                    c3=(b[0]*b[0] - b[1]*b[1] + b[0]*b[1])*a[2]
                else:
                    c1=(-a[0]+a[1])*b[2]
                    c2=        a[0]*b[2]
                    c3=        b[1]*a[2]
            else:
                c1=a[0]*b[2]
                c2=a[1]*b[2]
                c3=b[0]*a[2]
            x=np.array([c1,c2,c3],dtype=np.int64)
            g=np.gcd.reduce(x)
            if g!=0:
                c1=c1/g
                c2=c2/g
                c3=c3/g
                if c3<0:
                    return np.array([int(-c1),int(-c2),int(-c3)],dtype=np.int64)
                elif c1==0 and c2==0:
                    return np.array([0,0,1])
                else:
                    return np.array([int(c1),int(c2),int(c3)],dtype=np.int64)
            else:
                print('ERROR_2:division error')
                return 

# 計算ボタン
if st.button("Calculate"):
    try:
        if c1 == 0 or c2 == 0:
            raise ZeroDivisionError(" ")
        elif operation == "addition":
            result = add([a1,b1,c1],[a2,b2,c2])
        elif operation == "subtraction":
            result = div([a1,b1,c1],[a2,b2,c2])
        elif operation == "multiplication":
            result = mul([a1,b1,c1],[a2,b2,c2])
        elif operation == "division":
            if a2 == 0 and b2 == 0:
                raise ZeroDivisionError(" ")
            result = div([a1,b1,c1],[a2,b2,c2])
        st.success(f"a: {result[0]}")
        st.success(f"b: {result[1]}")
        st.success(f"c: {result[2]}")
    except Exception as e:
        st.error(f"Error: {e}")
