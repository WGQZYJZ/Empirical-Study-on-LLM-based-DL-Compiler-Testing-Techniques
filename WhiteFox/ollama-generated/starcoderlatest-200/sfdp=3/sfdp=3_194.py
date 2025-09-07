t1 = (q * key).sum(-2) # Sum along the last two dimensions of a pairwise multiply with the query tensor and the key tensor
e1 = torch.nn.functional.softmax(t1, dim=-1)  # Apply softmax to the output of the sum operation
output  = (v * e1).sum(-2) # Sum along the last two dimensions of a pairwise multiply with the value tensor and the scaled dot product
t1 = (q * key).sum(-2) # Sum along the last two dimensions of a pairwise multiply with the query tensor and the key tensor
t2 = (k * q).sum(-3) # Sum along the third dimension of a pairwise multiply with the key tensor and the query tensor
e1 = torch.nn.functional.softmax(t1 + t2, dim=-1)  # Apply softmax to the output of the sum operation
output  = (v * e1).sum(-2) # Sum along the last two dimensions of a pairwise multiply with the value tensor and the scaled dot product
