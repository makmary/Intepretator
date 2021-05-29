application

	integer a, b, r
	string l, s
	boolean t
	
	a := 1 
	b := 1
	t := true
	
	robot 1 1

	function of integer just_go (a) begin forward forward forward forward end 
		return a 

	function of integer go_back (a) begin back back back back end
		return a

	function of integer change_ver (...) begin rotate_left rotate_left end
		return r

	function of integer small_rot (...) begin rotate_left rotate_left rotate_left end
		return l

	function of integer search (r) begin forward rotate_right lms r := lns end
		return r

	function of integer go_around (...) begin forward left left back rotate_left end
		return a	

	function of integer go_round (...) begin back right right forward end
		return a

	do begin a := a + 1 just_go (...) small_rot (...) end until a < 1
	
	do begin forward rotate_right lms r := lns end until b <> r
	small_rot (...)

		a := 0
	do begin a := a + 1 just_go (...) small_rot (...) end until a < 1

		b := 0 
	do begin b := b + 1 go_around (l) just_go (...) end until b < 1
	rotate_right
		lms 
		r := lns

	if 20 > 5 then begin just_go (a) go_around (...) end
		just_go (a)
		go_round (...)
		rotate_right
	
	function of boolean test (...) if search() return true else return false
		just_go (...)
	
finish
