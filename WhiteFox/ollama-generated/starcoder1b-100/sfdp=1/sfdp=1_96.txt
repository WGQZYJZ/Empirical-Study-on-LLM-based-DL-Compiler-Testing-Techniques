
class Model(torch.nn.Module):
    def __init__(self, d_k=None, d_v=None):
        super().__init__()
        self.d_k = d_k
        self.d_v = d_v
        self.w_q = torch.nn.Parameter(torch.randn(d_k))  # Random initialized weight matrix
        self.w_kv = torch.nn.Parameter(torch.randn(d_k, d_v))  # Random initialized weight matrix
 
    def forward(self, x, context):
        v = torch.matmul(x, self.w_q)  # Compute the dot product of the input and the weight matrix
        k = torch.matmul(context, self.w_kv)  # Compute the dot product of the context vector and the weight matrix
        dk = torch.diag(k)  # Calculate the diagonal of the kernel matrix
        dk = dk / (dk @ dk.transpose(-2, -1))  # Normalize the kernel by dividing its diagonal element-wisely with its off-diagonal element-wise square root element-wisely
        context_vector = torch.matmul(context, dk)  # Compute the dot product of the context vector and the kernel matrix
        v = torch.nn.functional.dropout(v, p=self.p)  # Apply dropout to the dot product
        output = v + context_vector  # Sum the dot product with the context vector
        return output


# Initializing the model
m = Model()
m.__init__()
m.eval()
