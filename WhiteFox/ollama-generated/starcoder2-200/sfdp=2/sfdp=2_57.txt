
class Attention(torch.nn.Module):
    def __init__(self, hidden_size: int = 768) -> None:
        super().__init__()
        self._hidden_size = hidden_size
 
    def forward(self, query, key, value): 
        scale_factor  = torch.sqrt(torch.tensor([float(query.shape[-1])])) # Calculate the square root of the size of the last dimension in the query tensor
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.75) # Drop out 25% of the elements in the softmax output tensor with probability 0.75
        output  = dropout_qk @ value
        return output


# Initializing the model