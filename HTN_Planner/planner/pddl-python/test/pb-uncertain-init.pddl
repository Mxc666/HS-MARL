

(define (problem BW-rand-3)
(:domain blocksworld)
(:objects b1 b2 b3 )
(:init
(on-table b1)
(clear b1)
(unknown (on-table b3))
(unknown (clear b3))
(unknown (on b3 b2))
(unknown (on-table b2))
(unknown (clear b2))
(unknown (on b2 b3))
(or
(not (on b3 b2))
(not (on b2 b3))
)
(or
(not (on b2 b3))
(not (on b3 b2))
)
(oneof
(clear b3)
(clear b2)
)
(oneof
(on-table b3)
(on-table b2)
)
(oneof
(on-table b3)
(on b3 b2)
)
(oneof
(on-table b2)
(on b2 b3)
)
(oneof
(clear b3)
(on b2 b3)
)
(oneof
(clear b2)
(on b3 b2)
)
)
(:goal
(and
(on b2 b1)
(on b3 b2))
)
)
