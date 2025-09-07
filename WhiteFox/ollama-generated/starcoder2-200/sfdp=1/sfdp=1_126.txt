
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        v1 = torch.matmul(input1, input2)
        v2 = v1 / 0.3456789 
        v3 = torch.nn.functional.softmax(v2)
        v4 = torch.nn.functional.dropout(v3, p=0.76)
        