
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat  = torch.nn.Parameter(
            torch.ones(4, 8, requires_grad=True))
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.mat)
        invsf  = 3 + ((torch.rand(2)*10).round() // 1).type(qk.dtype)[0] / 16
        vsf = (torch.rand(2)+1).type(qk.dtype)[0].mul_(1/invsf)
        sfk = qk * invsf 
        softmaxqk = torch.nn.functional.softmax(sfk, dim=-1)
        dropoutqk = torch.nn.functional.dropout(softmaxqk, p=dropout_p)
        output  = dropoutqk.matmul(x1)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(20, 4 ,8 )
 
__output__  = m(x1)
 
