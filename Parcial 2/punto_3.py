def postorden(preor, inor):
    if len(preor) == 0 or len(inor) == 0:
        return ''
    if len(preor) == 1 or len(inor) == 1:
        return preor
    post, inor_i, inor_d, preor_i, preor_d = '', '',  '', '', '' 
    i = 0
    while inor[i] != preor[0]:
        inor_i = inor_i + inor[i]
        i += 1
    i += 1
    while i < len(inor):
        inor_d = inor_d + inor[i]
        i += 1
    for char in preor:
        if char in inor_i:
            preor_i = preor_i + char
        if char in inor_d:
            preor_d = preor_d + char
    post = post + postorden(preor_i, inor_i) + postorden(preor_d, inor_d) + preor[0]
    return post


def main():
    ans = postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ")
    print(ans)


if __name__ == '__main__':
    main()
