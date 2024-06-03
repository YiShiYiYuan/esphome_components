
# Example for components

## BL0906

Generation yaml with python:

```python
for i in '1,2,3,4,5,6,sum'.split(','):
    print(f"""    Energy_{i}: 
      id: energy_{i}
      name: 'Energy_{i}'""")
    
for i in '1,2,3,4,5,6,sum'.split(','):
    print(f"""  - platform: copy
    name: 'Energy_{i}'
    id: Energy_{i}_persist
    source_id: Energy_{i}
    filters:
      - lambda: |-
          if(id(id_Energy_{i}_lastvalue) == 0.0)
          {{
            id(id_Energy_{i}_lastvalue) = id(Energy_{i}).state;
          }}

          if(x < id(id_Energy_{i}_persist))
          {{
            float delta =  x - id(id_Energy_{i}_lastvalue);
            id(id_Energy_{i}_persist) += delta;
            id(id_Energy_{i}_lastvalue) = x;
          }} else {{
            id(id_Energy_{i}_persist) = x;
          }}
          return id(id_Energy_{i}_persist);""")

for i in '1,2,3,4,5,6,sum'.split(','):
    print(f"""  - id: id_Energy_{i}_persist
    type: float
    restore_value: yes
    initial_value: '0.0'
  - id: id_Energy_{i}_lastvalue
    type: float
    restore_value: no
    initial_value: '0.0'""")
```

## CMCC sy7t609

铁通插排，购买时附带的软件及配置文件。

```
https://bbs.hassbian.com/thread-23734-1-1.html
https://bbs.hassbian.com/thread-23623-1-1.html
参考资料
默认wifi密码 12345678
```