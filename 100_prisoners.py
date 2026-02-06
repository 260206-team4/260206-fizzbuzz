    # ------------------------------------------

    # [그룹 2] 팀원 2: 박스 체이싱(Cycle) 내부 로직 (Keyword: def 2)

    # ------------------------------------------

    def cycleIncluding(target):

        '''특정 죄수가 자신의 번호를 찾는 경로(Cycle) 추적 구현'''

        boxChain = [target]

        v = shuffled[target - 1]

        while v != target:

            boxChain.append(v)

            v = shuffled[v - 1]

        return boxChain



    def boxCycle(targets):

        '''전체 대상 중 첫 번째 타겟의 사이클을 추출하고 남은 타겟 반환'''

        if targets:

            boxChain = cycleIncluding(targets[0])

            return Just((

                difference(targets[1:])(boxChain),

                boxChain

            )) if limit >= len(boxChain) else Nothing()

        else:

            return Nothing()



    return int(n == sum(map(len, unfoldr(boxCycle)(xs))))
