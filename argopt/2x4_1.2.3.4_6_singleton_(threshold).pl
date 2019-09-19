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

myAsm(tau6).
contrary(tau6, C(tau6)).
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

myRule(C(tau6), [a13-3, a14-4]).
myRule(C(tau6), [a23-3, a24-4]).
myRule(C(tau6), [a11-1, a12-2, a14-4]).
myRule(C(tau6), [a21-1, a22-2, a24-4]).
myRule(C(tau6), [a11-1, a13-3, a14-4]).
myRule(C(tau6), [a21-1, a23-3, a24-4]).
myRule(C(tau6), [a12-2, a13-3, a14-4]).
myRule(C(tau6), [a22-2, a23-3, a24-4]).
myRule(C(tau6), [a11-1, a12-2, a13-3, a14-4]).
myRule(C(tau6), [a21-1, a22-2, a23-3, a24-4]).

myPrefLT(a11-1, tau6).
myPrefLT(a12-2, tau6).
myPrefLT(a13-3, tau6).
myPrefLT(a14-4, tau6).
myPrefLT(a21-1, tau6).
myPrefLT(a22-2, tau6).
myPrefLT(a23-3, tau6).
myPrefLT(a24-4, tau6).

myPrefLT(a11-1, a21-1). 
myPrefLT(a22-2, a12-2).
myPrefLT(a23-3, a13-3). 
myPrefLT(a14-4, a24-4).
