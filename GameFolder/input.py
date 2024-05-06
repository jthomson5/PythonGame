from typing import Optional
import tcod.event
from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):       # Sends event to proper method
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:    # Return action subclass or None
        action : Optional[Action] = None        # Holds subclass
        key = event.sym     # Holds key that was pressed
        # Handles potential key presses, and calls MovementAction
        if key == tcod.event.KeySym.w:
            action = MovementAction(dx = 0, dy = -1)
        if key == tcod.event.KeySym.s:
            action = MovementAction(dx = 0, dy = 1)
        if key == tcod.event.KeySym.a:
            action = MovementAction(dx = -1, dy = 0)
        if key == tcod.event.KeySym.d:
            action = MovementAction(dx = 1, dy = 0)
        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        return action