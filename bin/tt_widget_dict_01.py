def generate_tt(key):
  if key == 0:
    # Events when clicked    
    grid1_1[0,3].on_click(on_button_clicked)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.1: AND Truth Table', 'info', '466px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_1])

  elif key == 1:
    # Events when clicked    
    grid1_2[0,3].on_click(on_button_clicked2)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.2: OR Truth Table', 'info', '466px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_2])

  elif key == 2:
    # Events when clicked    
    grid1_3[0,2].on_click(on_button_clicked3)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.3: NOT Truth Table', 'info', '361px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_3])

  elif key == 3:
    # Events when clicked    
    grid1_4[0,3].on_click(on_button_clicked4)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.4: NOR Truth Table', 'info', '466px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_4])

  elif key == 4:
    # Events when clicked    
    grid1_5[0,3].on_click(on_button_clicked5)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.5: NAND Truth Table', 'info', '466px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_5])

  elif key == 5:
    # Events when clicked    
    grid1_6[0,3].on_click(on_button_clicked6)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.6: XOR Truth Table', 'info', '466px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_6])

  elif key == 6:
    # Events when clicked    
    grid1_7[0,3].on_click(on_button_clicked7)
    # Create the head tab
    header_button = create_expanded_button('Figure 1.6: XNOR Truth Table', 'info', '466px')
    # Display the widgets
    widgets.VBox([widgets.HTML(value="<span id='1.1'></span>"), AppLayout(header=header_button,footer=None),grid1_7])

  elif key == 7:
    
  
