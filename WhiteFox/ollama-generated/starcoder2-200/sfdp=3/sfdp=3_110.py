
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,1)
 
    def forward(self, x0):
        q = 2. * (x0 + 1.)
        k = 3. / ((q.abs() ** 2).sqrt()) 
        v = 4 * (k - (-1)) ** 2
        
        scaled_qk = torch.matmul(q, k)        
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.)
        output = dropout_qk.mul_(v)
        return output
        
# Initializing the model       
m = Model()

 # Inputs to the model
x1  = torch.randn(256,3,)   # Tensor of size (n, 3)
__output__  = m(x0)


