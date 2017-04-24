output = zeros(1000000,5);
pickup = zeros(1,15);
pickall = 0;
for i = 1:1000000
    output(i,:) = [0,0,0,0,0];
    for s = 1:6
        rr = rand();
        if rr<0.1
            output(i,1) = output(i,1)+1;
        elseif 0.1 <=rr && rr< 0.1 + 0.25
            output(i,2) = output(i,2)+1;
        elseif 0.1+0.25 <= rr && rr < 0.1+0.25+0.3
            output(i,3) = output(i,3)+1;
        elseif 0.1+0.25+0.3 <= rr && rr< 0.1+0.25+0.3+0.25
            output(i,4) = output(i,4)+1;
        else
            output(i,5) = output(i,5)+1;
        end
                
    end
    if all(output(i,1:5)==[2,1,1,1,1])
    %if all(output(i,1:5)>0 )
        pickup(1) = pickup(1) + 1;
    end
    
    if all(output(i,1:5)==[1,2,1,1,1])
    %if all(output(i,1:5)>0 )
        pickup(2) = pickup(2) + 1;
    end
    
    if all(output(i,1:5)==[1,1,2,1,1])
    %if all(output(i,1:5)>0 )
        pickup(3) = pickup(3) + 1;
    end
    
    if all(output(i,1:5)==[1,1,1,2,1])
    %if all(output(i,1:5)>0 )
        pickup(4) = pickup(4) + 1;
    end
    
    if all(output(i,1:5)==[1,1,1,1,2])
    %if all(output(i,1:5)>0 )
        pickup(5) = pickup(5) + 1;
    end
    
    if all(output(i,1:5)==[2,2,1,1,0])
    %if all(output(i,1:5)>0 )
        pickup(6) = pickup(6) + 1;
    end
    
    if all(output(i,1:5)==[1,2,2,1,0])
    %if all(output(i,1:5)>0 )
        pickup(7) = pickup(7) + 1;
    end
    
    if all(output(i,1:5)==[1,1,2,2,0])
    %if all(output(i,1:5)>0 )
        pickup(8) = pickup(8) + 1;
    end
    
    if all(output(i,1:5)==[2,1,1,2,0])
    %if all(output(i,1:5)>0 )
        pickup(9) = pickup(9) + 1;
    end
    
    if all(output(i,1:5)==[2,1,2,1,0])
    %if all(output(i,1:5)>0 )
        pickup(10) = pickup(10) + 1;
    end
    
    if all(output(i,1:5)==[1,2,1,2,0])
    %if all(output(i,1:5)>0 )
        pickup(11) = pickup(11) + 1;
    end
    
        
    if all(output(i,1:5)==[3,1,1,1,0])
    %if all(output(i,1:5)>0 )
        pickup(12) = pickup(12) + 1;
    end
    
    if all(output(i,1:5)==[1,3,1,1,0])
    %if all(output(i,1:5)>0 )
        pickup(13) = pickup(13) + 1;
    end
    
    if all(output(i,1:5)==[1,1,3,1,0])
    %if all(output(i,1:5)>0 )
        pickup(14) = pickup(14) + 1;
    end
    
    if all(output(i,1:5)==[1,1,1,3,0])
    %if all(output(i,1:5)>0 )
        pickup(15) = pickup(15) + 1;
    end
    %if all(output(i,1:5)==[1,1,1,3,0])
    if all(output(i,1:4)>0 )
        pickall = pickall + 1;
    end
    
end