myAsm(a11-1).
myAsm(a12-2).
myAsm(a13-3).
myAsm(a14-4).
myAsm(a21-1).
myAsm(a22-2).
myAsm(a23-3).
myAsm(a24-4).
contrary(a11-1, C(a11-1)).
contrary(a12-2, C(a12-2)).
contrary(a13-3, C(a13-3)).
contrary(a14-4, C(a14-4)).
contrary(a21-1, C(a21-1)).
contrary(a22-2, C(a22-2)).
contrary(a23-3, C(a23-3)).
contrary(a24-4, C(a24-4)).

myAsm(gamma1).
contrary(gamma1, C(gamma1)).
myAsm(gamma2).
contrary(gamma2, C(gamma2)).
myAsm(gamma3).
contrary(gamma3, C(gamma3)).
myAsm(gamma4).
contrary(gamma4, C(gamma4)).

myAsm(inf).
contrary(inf, C(inf)).

myRule(C(inf), [inf]).
myRule(C(inf), [f1, f2, f3, f4]).

myRule(f1, [a11-1]).
myRule(f1, [a21-1]).
myRule(f2, [a12-2]).
myRule(f2, [a22-2]).
myRule(f3, [a13-3]).
myRule(f3, [a23-3]).
myRule(f4, [a14-4]).
myRule(f4, [a24-4]).

myRule(C(a11-1), [a21-1]).
myRule(C(a21-1), [a11-1]).
myRule(C(a12-2), [a22-2]).
myRule(C(a22-2), [a12-2]).
myRule(C(a13-3), [a23-3]).
myRule(C(a23-3), [a13-3]).
myRule(C(a14-4), [a24-4]).
myRule(C(a24-4), [a14-4]).

myRule(C(gamma1), [a13-3, a14-4]).
myRule(C(gamma2), [a23-3, a24-4]).
myRule(C(gamma3), [a11-1, a12-2, a14-4]).
myRule(C(gamma4), [a21-1, a22-2, a24-4]).

myRule(C(a13-3), [gamma1, a14-4]).
myRule(C(a14-4), [a13-3, gamma1]).
myRule(C(a23-3), [gamma2, a24-4]).
myRule(C(a24-4), [a23-3, gamma2]).
myRule(C(a11-1), [gamma3, a12-2, a14-4]).
myRule(C(a12-2), [a11-1, gamma3, a14-4]).
myRule(C(a14-4), [a11-1, a12-2, gamma3]).
myRule(C(a21-1), [gamma4, a22-2, a24-4]).
myRule(C(a22-2), [a21-1, gamma4, a24-4]).
myRule(C(a24-4), [a21-1, a22-2, gamma4]).

myPrefLT(a11-1, gamma3).
myPrefLT(a12-2, gamma3).
myPrefLT(a13-3, gamma1).
myPrefLT(a14-4, gamma1).
myPrefLT(a14-4, gamma3).
myPrefLT(a21-1, gamma4).
myPrefLT(a22-2, gamma4).
myPrefLT(a23-3, gamma2).
myPrefLT(a24-4, gamma2).
myPrefLT(a24-4, gamma4).
