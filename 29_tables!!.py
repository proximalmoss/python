#tables 
for i in range(2,21):
    for j in range(11):
        with open (f"tables/multiplication_table_of_{i}","w") as f:
            f.write(f"{i}x{j}={i*j}\n")
        break