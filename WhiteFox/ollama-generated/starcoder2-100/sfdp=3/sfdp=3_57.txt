
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = 1e-30
        self.dropout = 0.2
        
    def forward(self, query, key, value):
        scale  = 1 / torch.sqrt(torch.tensor([query.shape[-1]]))
        qk  = torch.matmul(query, key.transpose(-2, -1)) * scale
        softmax_qk  = qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        output  = dropout_qk @ value 
        return output


m = Model()
m(torch.randn([2048]), torch.randn([2048]), torch.randn([512]))
