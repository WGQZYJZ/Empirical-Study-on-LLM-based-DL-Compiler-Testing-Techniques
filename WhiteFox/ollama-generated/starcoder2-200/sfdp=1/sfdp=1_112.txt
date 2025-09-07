
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(64, 32)
 
    def forward(self, qk):
        scaled_qk = self.matmul(qk).div(0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        return dropout_qk @ value


# Initializing the model<|end_of_model|>
m  = Model()
 
# Input to the model
query  = torch.randn(16, 32) + 4.5; key  = torch.randn(16, 32);  value  = <KEY>

