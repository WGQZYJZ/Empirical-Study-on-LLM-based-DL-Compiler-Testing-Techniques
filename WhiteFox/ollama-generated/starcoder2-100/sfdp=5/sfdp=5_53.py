x  = torch.nn.Embedding(32000, 1024)  # Declare embedding layer with 32k vocab size and 1024 output dimensionality
l1 = torch.nn.LSTM(input_size=x.embedding_dim, hidden_size=512)  # Create an LSTM layer with 1024 input feature size to a hidden state of 512
l2 = torch.nn.LSTM(input_size=512 + x.embedding_dim, hidden_size=x.embedding_dim // 8)  # Add the embedding dimension (in this case, 1024//8) to the LSTM input size, and then create another LSTM layer that has an input feature size of 768

l3 = torch.nn.LSTM(input_size=x.embedding_dim + x.embedding_dim // 8, hidden_size=(x.embedding_dim + x.embedding_dim) // 4) # Add the output dimensionality (512 + 512//8) to the LSTM input size and then create another LSTM layer that has an input feature size of 3072
l4 = torch.nn.LSTM(input_size=(x.embedding_dim+ x.embedding_dim)//4, hidden_size=x.embedding_dim*512) # Add the output dimensionality (3072) to the LSTM input size and then create another LSTM layer that has an input feature size of 6912
l5 = torch.nn.LSTM(input_size=(x.embedding_dim + x.embedding_dim)*512, hidden_size=math.sqrt(x.embedding_dim)) # Add the output dimensionality (6912) to the LSTM input size and then create another LSTM layer that has an input feature size of 407
