
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale = torch.tensor([1 / math.sqrt(query.shape[-1])], requires_grad=False).to('cuda' if torch.cuda.is_available() else 'cpu')  # Set a constant to divide
        inv_scale = torch.inverse(scale)  # Compute the inverse of the constant above
        dot = query.matmul(key.transpose(-2, -1))  # Compute the dot product of the query and key
        scaled_dot = dot * scale[0]  # Scale by the constant before dividing it in the previous step with softmax (this is actually unnecessary because the dropout mask will divide by zero)
        softmax_dot = scaled_dot.softmax(dim=-1)  # Apply softmax to the scaled dot product,
        masked_softmax = softmax_dot / inv_scale[0]  # Divide the output of the softmax by the inverse scale factor before applying dropout (this is actually unnecessary because the dropout mask will divide by zero)
        drop = torch.nn.functional.dropout(masked_softmax, p=p).to('cuda' if torch.cuda.is_available() else 'cpu')  # Apply dropout to the softmax output
        return drop @ value  # Compute the dot product of the dropout output and a value


# Initializing the model