The model should contain the following pattern:
return torch.matmul(attn, value)  # Compute the weighted sum between query and key
return (input @ attention).sum(dim=-1)  # Calculate the weighted sum between input and the projected attention values
