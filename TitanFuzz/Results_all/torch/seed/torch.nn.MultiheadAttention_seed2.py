input_data = torch.randn(2, 3, 10)
input_data_2 = torch.randn(2, 3, 10)
attn = torch.nn.MultiheadAttention(embed_dim=10, num_heads=2)
(output, attn_weights) = attn.forward(input_data, input_data_2, input_data_2)