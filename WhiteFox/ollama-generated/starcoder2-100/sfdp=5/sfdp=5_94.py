
class MyModel(nn.Module):
    def __init__(self, d_k=64, nhead=8):
        super().__init__()
        self.linear1 = nn.Linear(320, 512)
        self.linear2 = nn.Linear(512, 196)

    def forward(self, query, key):

        q_proj = self.linear1(query)
        k_proj = self.linear2(key)

        dot_product = (q_proj * k_proj).sum(-1) # this is the dot product
        output = nn.functional.softmax(dot_product, dim=-1)
        return  output

model = MyModel()
