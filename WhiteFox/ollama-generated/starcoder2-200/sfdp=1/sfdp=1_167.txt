
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 30)
        self.key = torch.nn.Linear(768, 30)
        self.value = torch.nn.Linear(768, 21)
 
    def forward(self, x):
        v1  = self.query(x) 
        v2  = self.key(v1) # Compute the dot product of the query and key tensors
        v3  = v2 / math.sqrt(768 * 0.5)  
        v4  = torch.nn.functional.softmax(v3, dim=dim_for_attentive)
        v5  = torch.nn.functional.dropout(v4, p=p) 
        return v5

