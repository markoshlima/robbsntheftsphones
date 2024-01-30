import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreditorComponent } from './preditor.component';

describe('PreditorComponent', () => {
  let component: PreditorComponent;
  let fixture: ComponentFixture<PreditorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PreditorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PreditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
