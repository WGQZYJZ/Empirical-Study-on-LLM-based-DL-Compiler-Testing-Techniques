A = torch.rand(3, 3)
(Q, R) = torch.linalg.qr(A)
QQ = Q.mm(Q.t())
RR = R.t().mm(R)