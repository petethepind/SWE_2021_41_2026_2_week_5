def isHappy(n):
  Input = n
  Loop_Check = set()
  while n not in Loop_Check:
    Loop_Check.add(n)
    stored_values = [i for i in str(n)]
    n = sum(int(i)**2 for i in stored_values)

  if n == 1:
    return True   
  return False

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")
