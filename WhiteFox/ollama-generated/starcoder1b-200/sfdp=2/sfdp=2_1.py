
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(128, 64)
 
    def forward(self, x1, x2):
        # Compute the dot product of the two input tensors (x1 and x2).
        # Scale by the inverse scale factor so that we can perform softmax
        v1 = self.attn(x1) * 0.5
        v2 = self.attn(x2) * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        # Apply dropout to the softmax output to keep the query's output within [0, 1]
        v4 = torch.nn.functional.dropout(
            torch.nn.functional.softmax(v3), p=self.dropout_p)
        v5 = v4.matmul(x2)
        return x1 * v5


# Initializing the model
m = Model()


