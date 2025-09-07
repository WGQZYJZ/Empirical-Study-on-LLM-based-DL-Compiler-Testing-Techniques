
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(768, 3072) # Apply linear transformation to the input embeddings of query and key tensors
        self.linear_k = torch.nn.Linear(768, 3072)
        self.matmul_qk = torch.nn.Linear(768, 1536)
 
    def forward(self, x):
        # Apply the linear transformation to the input embeddings of query and key tensors
        q = self.linear_q(x[0])
        k = self.linear_k(x[1])
        # Compute the dot product of the query and key tensors
        v1 = torch.matmul(q, k)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
 
        # Apply softmax to the scaled dot product
        softmax_qk = F.softmax(self.matmul_qk(x[0]), dim=-1)

        # Apply dropout to the softmax output
        v7 = torch.nn.functional.dropout(softmax_qk, p=0.2)

        # Compute the dot product of the dropout output and the value tensor
        output = torch.matmul(v7, v6)
        
        return output


# Initializing the model
m = Model()
x = (torch.randn(1, 3072), torch.randn(1, 3072))
