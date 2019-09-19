myAsm(a11-1).
myAsm(a12-2).
myAsm(a21-1).
myAsm(a22-2).
myAsm(a31-1).
myAsm(a32-2).
contrary(a11-1, C(a11-1)).
contrary(a12-2, C(a12-2)).
contrary(a21-1, C(a21-1)).
contrary(a22-2, C(a22-2)).
contrary(a31-1, C(a31-1)).
contrary(a32-2, C(a32-2)).

myAsm(tau2).
contrary(tau2, C(tau2)).
myAsm(inf).
contrary(inf, C(inf)).

myRule(C(inf), [inf]).
myRule(C(inf), [f1, f2]).

myRule(f1, [a11-1]).
myRule(f1, [a21-1]).
myRule(f1, [a31-1]).
myRule(f2, [a12-2]).
myRule(f2, [a22-2]).
myRule(f2, [a32-2]).

myRule(C(a11-1), [a21-1]).
myRule(C(a11-1), [a31-1]).
myRule(C(a21-1), [a11-1]).
myRule(C(a21-1), [a31-1]).
myRule(C(a31-1), [a11-1]).
myRule(C(a31-1), [a21-1]).
myRule(C(a12-2), [a22-2]).
myRule(C(a12-2), [a32-2]).
myRule(C(a22-2), [a12-2]).
myRule(C(a22-2), [a32-2]).
myRule(C(a32-2), [a12-2]).
myRule(C(a32-2), [a22-2]).

myRule(C(tau2), [a11-1, a12-2]).
myRule(C(tau2), [a21-1, a22-2]).
myRule(C(tau2), [a31-1, a32-2]).

myRule(C(a11-1), [tau2, a12-2]).
myRule(C(a12-2), [a11-1, tau2]).
myRule(C(a21-1), [tau2, a22-2]).
myRule(C(a22-2), [a21-1, tau2]).
myRule(C(a31-1), [tau2, a32-2]).
myRule(C(a32-2), [a12-2, tau2]).

myPrefLT(a11-1, tau2).
myPrefLT(a12-2, tau2).
myPrefLT(a21-1, tau2).
myPrefLT(a22-2, tau2).
myPrefLT(a31-1, tau2).
myPrefLT(a32-2, tau2).

myPrefLT(a21-1, a11-1).
myPrefLE(a31-1, a21-1).
myPrefLE(a21-1, a31-1).

myPrefLT(a22-2, a12-2).
myPrefLE(a32-2, a22-2).
myPrefLE(a22-2, a32-2).
