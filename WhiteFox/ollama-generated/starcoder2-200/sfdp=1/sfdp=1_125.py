
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        self.softmax_qk = torch.nn.Softmax()  # Create a Softmax operator to perform softmax on the scaled dot products
        self.dropout = torch.nn.Dropout(p=0)  # Create an instance of Dropout to apply dropout

    def forward(self, qk):
        self.v1  = self.qk + 1 
        self.v2  = self.qk * self.v1  # Compute the dot product of the scaled dot products and v1

        self.v3_softmax = self.softmax_qk(self.v2)  # Apply softmax to the scaled dot product
        self.v4_drop = self.dropout(self.v3_softmax, p=0) 
        self.v5_matmul = self.v4 * self.value  # Compute the dot product of the dropout output and the value tensor

        return self.v5


# Initializing model