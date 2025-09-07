
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(dim))
        self.key   = torch.nn.Parameter(torch.randn(dim))
 
    def forward(self, x1, x2=None, mask=None):
        scaled_qk  = torch.matmul(x1, self.query).transpose(-2, -1) # Compute the dot product of the query and key tensors
        softmax_qk = torch.softmax(scaled_qk) # Apply softmax to the scaled dot product
 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p) # Apply dropout to the softmax output
        attention  = self.attn_scale * dropout_qk

        if mask is not None:
            # Attention scores should be masked with zeros that are equal or larger than the value in the corresponding positions of the original inputs. 
            attention[mask < -10] = 0 
 
        return x2 + torch.matmul(attention, self.value)
 
    def extra_repr(self):
        return f"scale: {self.attn_scale}, dropout: {self.p}"


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # This class is not finished yet. Please refer to the comments in `attention.py` file for details.
        self.attn1 = Attention(dim=64)
 
    def forward(self, x1, x2=None):
        return self.attn1(x1, x2)


# Initializing the model
m  = Model()

# Inputs to the model
__query_tensor__ = torch.randn(batch_size, 3, dim1, dim2)
__value_tensor__ = torch.randn(num_buckets, hidden_dim * num_heads ** 0.5)
__output__  = m(__query_tensor__, __value_tensor__)

