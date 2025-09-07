
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(x3, x4)
        return (v1 + v2).type(torch.FloatTensor)


m  = Model()

inputs_for_model  = [
    torch.randn([3, 5]), # input tensor for the first matrix multiplication
    torch.randn([3, 6]), # input tensor for the first matrix multiplication
 
    torch.randn([4, 7]), # input tensor for the second matrix multiplication 
    torch.randn([8, 10])# input tensor for the second matrix multiplication
]
