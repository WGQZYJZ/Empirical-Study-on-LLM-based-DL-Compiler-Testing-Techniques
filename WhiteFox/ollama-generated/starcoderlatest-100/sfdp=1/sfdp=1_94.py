output = torch.relu(input)  # Apply ReLU activation to the input
output = torch.add(output, bias)  # Add the bias to the output
output = F.dropout(output, p=0.25, training=training) # Apply dropout with probability 0.25 during training
