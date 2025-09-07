
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 10
        self.dropout = torch.nn.Dropout(p=0)

    def forward(self, query, key, value):
        v2  = self.scale * (query @ key).transpose(-2,-1)
        v3  = nn.functional.softmax(v2, dim=-1) # dropout here?
        v5  = torch.nn.functional.dropout(v4, p=self.dropout_p, training=self._is_training) # softmax here?
        v6  = self.scale * v3 @ value
        return v7

# Initializing the model
m1  = Model()


# Inputs to the model:
q1  = torch.randn(4,20)  # batch size = 4; query is a matrix of shape (4 x 20)
k1  = torch.randn(32,480)  # batch size = 32 ; key and value are matrices of shape (32 x 480)


x1  = m1(q1, k1)
